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
        
        self.BG_COLOR = (0,0,0)
        
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
                for entity in self.entities:
                    entity.update(self.tick_rate)
                    
                for collision in self.currentArea.findCollisions():
                  collision[0].collide(collision[1])
                  collision[1].collide(collision[0])
                
                for entity in self.entities:
                    entity.render(self.screen)
                
                pygame.display.update()
            
            	self.last_update = get_ticks()
