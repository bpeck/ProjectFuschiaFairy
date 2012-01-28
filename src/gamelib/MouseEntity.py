import pygame
from pygame.rect import Rect
from pygame import Surface
from pygame import draw

from Entity import Entity
from InputListener import InputListener


class MouseEntity(Entity, InputListener):
    
    def __init__(self):
        self.name = 'MouseEntity'
        self.rect = Rect(0,0,25,25)
        self.pos = [0.0,0.0]
        self.pos[0] = -self.rect.center[0]
        self.pos[1] = -self.rect.center[1]
        
        self.image = Surface(self.rect[2:])
        self.image.set_colorkey((0,0,0))
        self.image.lock()
        draw.circle(self.image, (255,255,255), self.rect.center, self.rect.w/2, 1)
        self.image.unlock()
    
    def processEvent(self, event, dT):
        if event.type == pygame.MOUSEMOTION:
            # center the position at the mouse
            self.pos[0] = event.pos[0] - self.rect.center[0]
            self.pos[1] = event.pos[1] - self.rect.center[1]
    
    
    
