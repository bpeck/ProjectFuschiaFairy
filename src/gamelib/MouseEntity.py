import pygame, math
from pygame.rect import Rect
from pygame import Surface
from pygame import draw

from Entity import Entity
from Accelerator import Accelerator
from InputListener import InputListener


from Data import *
from Vect2 import Vect2

class MouseEntity(InputListener, Accelerator):

    def __init__(self):
        Accelerator.__init__(self, 5.0, 0.0, 4.0)
        self.name = 'MouseEntity'
        self.mouse_pos = Vect2([0.0, 0.0])
        self.origImage = pygame.image.load('data/mousePlayer.png')
        self.image =  self.origImage
        self.mouseOffset = Vect2(self.image.get_rect().center)
        self.rotate = 45
        self.radius = float(self.image.get_width()) / 2.0

    def processEvent(self, event, dT=0):
        if event.type == pygame.MOUSEMOTION:
            # center the position at the mouse
            oldPos = self.mouse_pos
            self.mouse_pos = Vect2(event.pos) - self.mouseOffset
            
    def update(self, dT=0):

            #c = self.image.get_rect().center
            self.image = pygame.transform.rotate(self.origImage,self.rotate)
            #self.image.get_rect().center = c
            self.rotate += 90
            if self.rotate > 360:
                self.rotate = 0
            #smoothing 
            self.pos = self.pos*0.9 + self.mouse_pos*0.1

