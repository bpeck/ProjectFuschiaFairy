# py imports
import os

# pygame imports
import pygame
from pygame.locals import *
from pygame.time import Clock

# our code imports
from Arena import Arena
from TestArena import TestArena
from Entity import Entity
from InputListener import InputListener

class Game(object):
    
    def __init__(self):
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        pygame.mouse.set_visible(0)
        pygame.display.set_caption("LAZAH POWAH!!!!")
        self.screen = pygame.display.set_mode( \
            resolution=(640, 480), \
            flags=pygame.FULLSCREEN)
    
        self.done = False
        
        self.currentArea = TestArena()
        
        self.entities = arena.getInitialEntities()
        self.inputListeners = arena.getInitialKeyListeners()
        
        # logic clock
        self.logicClock = Clock()
        self.logicClock.tick()
        self.LOGIC_CLOCK_RATE = 100
        self.LOGIC_TIME_SINCE_UPDATE = self.LOGIC_CLOCK_RATE
        
        # rendering clock
        self.renderClock = Clock()
        self.renderCLock.tick()
        self.RENDER_CLOCK_RATE = 100
        self.RENDER_TIME_SINCE_UPDATE = self.RENDER_CLOCK_RATEW
    
    def gameLoop(self):
        if self.done:
            return
    
        # update timers
        logicDt = self.logicClock.tick()
        LOGIC_TIME_SINCE_UPDATE += logicDt
        
        renderDt = self.renderClock.tick()
        RENDER_TIME_SINCE_UPDATE = renderDt
        
        # logic update
        if LOGIC_TIME_SINCE_UPDATE >= LOGIC_CLOCK_RATE:
            # process events
            for e in pygame.event.get():
                if e.type == QUIT:
                    print 'pygame QUIT event received, bailing.'
                    sys.exit()
                if e.type in [KEYDOWN, KEYUP, MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP]:
                    for listener in self.inputListeners:
                        listener.processEvent(e. logicDt)
            
            # update entities
            for entity in self.entities:
                entity.update(logicDt)
        
        # render update
        if RENDER_TIME_SINCE_UPDATE >= RENDER_CLOCK_RATE:
            for entity in self.entities:
                entity.render(self.screen, renderDt)
        
