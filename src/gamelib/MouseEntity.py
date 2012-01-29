import pygame
from pygame.rect import Rect
from pygame import Surface
from pygame import draw

from Entity import Entity
from InputListener import InputListener


from Data import *


from Vect2 import Vect2


class MouseEntity(Entity, InputListener):
    
    def __init__(self):
        Entity.__init__(self)
        self.name = 'MouseEntity'

        #self.rect = Rect(0,0,25,25)
        self.pos = [0.0,0.0]
       # self.pos[0] = -self.rect.center[0]
       # self.pos[1] = -self.rect.center[1]
        self.mouse_pos = Vect2((0, 0))
        self.image = pygame.image.load('data/mousePlayer.png')
       # self.image.set_colorkey((0,0,0))
       # self.image.lock()
      #  draw.circle(self.image, (255,255,255), self.rect.center, self.rect.w/2, 1)
      #  self.image.unlock()
    
    def processEvent(self, event, dT=0):
        if event.type == pygame.MOUSEMOTION:
            # center the position at the mouse
            self.pos[0] = event.pos[0] - self.image.get_rect().center[0]
            self.pos[1] = event.pos[1] - self.image.get_rect().center[1]
            self.mouse_pos = Vect2(event.pos)
    
    

    
    def update(self, dT=0):
        self.pos = self.mouse_pos
