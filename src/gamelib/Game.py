# py imports
import os, sys, time, random, math

# pygame imports
import pygame
from pygame.locals import *
from pygame.time import get_ticks
import pygame.sprite

# our code imports
from Arena import Arena
from TestArena import TestArena
from Entity import Entity
from InputListener import InputListener
from Prey import Prey
from Predator import Predator
#from Collision import Collision

import Variables
from Variables import *
from Data import *

class Game(object):
    
    def __init__(self, screen):
        self.screen = screen
        self.currentLevel = 0
        self.done = False
        self.deadPredator = []
        self.deadPrey = []
        self.currentArea = TestArena(screen ,self.currentLevel)
        
        self.entities = self.currentArea.getInitialEntities()
        self.inputListeners = self.currentArea.getInitialKeyListeners()
        self.accelerators = self.currentArea.getInitialAccelerators()
        
        self.BG_COLOR = (0,0,0)
        
        # le collision detection hack of the centry
        self.DIST_CUTOFF = 20 # pixels
        # keys Enity -> [Collision] list of collision objs involving that entity
        self.collisions = {}
        self.closest = {}
        
        # logic clock
        self.tick_rate = 30
        self.last_update = 0
        print 'Entering game loop'
        self.gameLoop()
    
    def gameLoop(self):
        bg = pygame.image.load("data/Background-640-Lev" + str(self.currentLevel +1) + ".png")
        while not self.done:
            for e in pygame.event.get():
                if e.type == QUIT:
                    print 'pygame QUIT event received, bailing.'
                    sys.exit()
                if e.type == KEYDOWN and e.key == Variables.escapeKey:
                   self.done = True
                if e.type in [KEYDOWN, KEYUP, MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP]:
                    for listener in self.inputListeners:
                        listener.processEvent(e)

            if self.last_update + self.tick_rate < get_ticks():
                start_of_frame = get_ticks()
            	#self.screen.fill(self.BG_COLOR)
                bg = pygame.image.load("data/Background.png")
                self.screen.blit(bg,[0,0])
                
                # update the arena  - doesnt do anything
                #self.currentArea.update(self.tick_rate)
                
                # update logic
                entitiesToRemove = []
                for entity in self.entities:
                    self.currentArea.collisionDetect(entity, self.tick_rate)
                    entity.update(self.tick_rate)
                    if entity.iDied ==1:
                        entitiesToRemove.append(entity)
                        continue
                    entity.render(self.screen)

                for e in entitiesToRemove:
                    if isinstance(e, Predator):
                        self.deadPredator.append(time.time())
                    if isinstance(e, Prey):
                        self.deadPrey.append(time.time())
                    self.entities.remove(e)
                    #print "removed a guy!"
                maxSize = 50.0
                minSize = 6.0
                # rotation accel rates
                maxRotVel = math.pi / 20.0
                maxRotAcc = math.pi / 40.0
                for i in self.deadPrey:
                    if time.time() > i +3:
                        size = minSize + random.random() * (maxSize - minSize)
                        pos = [0.0,0.0]
                        pos[0] += int(random.random() * screenW)
                        pos[1] += int(random.random() * screenH)            
                        prey = Prey(size, pos, maxRotVel, maxRotAcc, self.currentArea)
                        self.entities.append(prey)
                        self.deadPrey.remove(i)
                for i in self.deadPredator:
                    if time.time() > i +3:
                        size = minSize + random.random() * (maxSize - minSize)
                        pos = [0.0,0.0]
                        pos[0] += int(random.random() * 640)
                        pos[1] += int(random.random() * 480)            
                        predator = Predator(size, pos, maxRotVel, maxRotAcc, self.currentArea)
                        self.entities.append(predator)
                        self.deadPredator.remove(i)
                # exert attract/repulse forces - this is shitty
                #self.currentArea.doAccelerators()

                self.last_update = get_ticks()
                
            pygame.display.update()
