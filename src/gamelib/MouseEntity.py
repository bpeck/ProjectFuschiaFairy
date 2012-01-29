import pygame
from pygame.rect import Rect
from pygame import Surface
from pygame import draw

from Entity import Entity
from Accelerator import Accelerator
from InputListener import InputListener
from Vect2 import Vect2

class MouseEntity(InputListener, Accelerator):
    
    def __init__(self):
        Accelerator.__init__(self, 5.0, 0.0, 4.0)
        self.name = 'MouseEntity'
        self.mouse_pos = Vect2([0.0, 0.0])
        self.image = pygame.image.load('data/mousePlayer.png')
        self.mouseOffset = Vect2(self.image.get_rect().center)
    
    def processEvent(self, event, dT=0):
        if event.type == pygame.MOUSEMOTION:
            # center the position at the mouse
            self.mouse_pos = Vect2(event.pos) - self.mouseOffset
    
    def update(self, dT=0):
        self.pos = self.mouse_pos
