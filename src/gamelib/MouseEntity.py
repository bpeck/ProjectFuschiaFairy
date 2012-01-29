import pygame
from pygame.rect import Rect
from pygame import Surface
from pygame import draw

from Entity import Entity
from InputListener import InputListener

from Vect2 import Vect2

class MouseEntity(Entity, InputListener):
    
    def __init__(self):
        Entity.__init__(self)
        self.name = 'MouseEntity'
        self.radius = 12
        self.rect = Rect(0, 0, self.radius*2, self.radius*2)
        
        self.mouse_pos = Vect2((0, 0))
        
        self.image = Surface(self.rect[2:])
        self.image.set_colorkey((0,0,0))
        self.image.lock()
        draw.circle(self.image, (255,255,255), (self.radius, self.radius), self.radius, 1)
        self.image.unlock()
    
    def processEvent(self, event, dT=0):
        if event.type == pygame.MOUSEMOTION:
            self.mouse_pos = Vect2(event.pos)
    
    def update(self, dT=0):
        self.pos = self.mouse_pos