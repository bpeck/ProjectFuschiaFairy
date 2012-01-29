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

        self.imgState = 0
        self.image1 = pygame.image.load('data/mousePlayer_1.png')
        self.image2 = pygame.image.load('data/mousePlayer_2.png')
        self.image3 = pygame.image.load('data/mousePlayer_3.png')

    def processEvent(self, event, dT=0):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.imgState = 1
        if event.type == pygame.MOUSEMOTION:
            # center the position at the mouse
            oldPos = self.mouse_pos
            self.mouse_pos = Vect2(event.pos) - self.mouseOffset
        if event.type == pygame.MOUSEBUTTONUP:
            self.imgState = 0
            self.image = self.origImage
            
    def bite(self):
        if self.imgState == 1:
            self.image = self.image1
            self.imgState += 1
        if self.imgState == 2:
            self.image = self.image2
            self.imgState += 1
        if self.imgState == 3:
            self.image = self.image3
 
    def update(self, dT=0):
            if self.imgState > 0:
                self.bite()
           
            #smoothing 
            self.pos = self.pos*0.9 + self.mouse_pos*0.1

