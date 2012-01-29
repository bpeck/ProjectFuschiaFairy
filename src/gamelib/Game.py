# py imports
import os, sys

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
from Collision import Collision
import Variables
from Variables import *
from Data import *

class Game(object):
    
    def __init__(self, screen):
        self.screen = screen
    
        self.done = False
        
        self.currentArea = TestArena(screen)
        
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
        self.tick_rate = 50
        self.last_update = 0
        print 'Entering game loop'
        self.gameLoop()
    
    def gameLoop(self):
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
            	#self.screen.fill(self.BG_COLOR)
                bg = pygame.image.load("data/Background.png")
                self.screen.blit(bg,[0,0])
                
                # update the arena  - doesnt do anything
                #self.currentArea.update(self.tick_rate)
                
                # update logic
                for entity in self.entities:
                    self.currentArea.collisionDetect(entity, self.tick_rate)
                    entity.update(self.tick_rate)
                    entity.render(self.screen)
                
                # exert attract/repulse forces - this is shitty
                #self.currentArea.doAccelerators()
                
                
                pygame.display.update()
            
            	self.last_update = get_ticks()
