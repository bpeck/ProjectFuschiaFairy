# py imports
import os, sys

# pygame imports
import pygame
from pygame.locals import *
from pygame.time import Clock
import pygame.sprite

# our code imports
from Arena import Arena
from TestArena import TestArena
from Entity import Entity
from InputListener import InputListener

import Variables
from Variables import *

class Game(object):
    
    def __init__(self, screen):
        self.screen = screen
    
        self.done = False
        
        self.currentArea = TestArena()
        
        self.entities = self.currentArea.getInitialEntities()
        self.inputListeners = self.currentArea.getInitialKeyListeners()
        
        self.BG_COLOR = (0,0,0)
        
        # logic clock
        self.logicClock = Clock()
        self.logicClock.tick()
        self.LOGIC_CLOCK_RATE = 100
        self.LOGIC_TIME_SINCE_UPDATE = self.LOGIC_CLOCK_RATE
        
        # rendering clock
        self.renderClock = Clock()
        self.renderClock.tick()
        self.RENDER_CLOCK_RATE = 100
        self.RENDER_TIME_SINCE_UPDATE = self.RENDER_CLOCK_RATE
        
        print 'Entering game loop'
        self.gameLoop()
    
    def gameLoop(self):
    
        while not self.done:
                
            # update timers
            logicDt = self.logicClock.tick()
            self.LOGIC_TIME_SINCE_UPDATE += logicDt
            
            renderDt = self.renderClock.tick()
            self.RENDER_TIME_SINCE_UPDATE += renderDt
            
            # logic update
            if self.LOGIC_TIME_SINCE_UPDATE >= self.LOGIC_CLOCK_RATE:
                # process events
                for e in pygame.event.get():
                    if e.type == QUIT:
                        print 'pygame QUIT event received, bailing.'
                        sys.exit()
                    if e.type == KEYDOWN and e.key == Variables.escapeKey:
                        self.done = True
                    if e.type in [KEYDOWN, KEYUP, MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP]:
                        for listener in self.inputListeners:
                            listener.processEvent(e, logicDt)
                
                # update entities
                for entity in self.entities:
                    entity.update(logicDt)
            
            # render update
            if self.RENDER_TIME_SINCE_UPDATE >= self.RENDER_CLOCK_RATE:
                self.screen.fill(self.BG_COLOR)
                for entity in self.entities:
                    entity.render(self.screen, renderDt)
                
                pygame.display.update()
        
