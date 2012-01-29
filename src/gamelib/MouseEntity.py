import pygame, math
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
        self.mouse_pos = Vect2([0.0, 0.0])
        self.origImage = pygame.image.load('data/mousePlayer.png')
        self.image =  self.origImage
        self.mouseOffset = Vect2(self.image.get_rect().center)
        self.rotate = 45


    def processEvent(self, event, dT=0):
        if event.type == pygame.MOUSEMOTION:
            # center the position at the mouse
            oldPos = self.mouse_pos
            self.mouse_pos = Vect2(event.pos) - self.mouseOffset
            
           # angle = math.degrees(math.atan2( oldPos[1]-self.mouse_pos[1], oldPos[0]-self.mouse_pos[0]))+180
            #self.rotate = angle
            #oRect = self.image.get_rect()
            #angle =
            
            #print angle 
            
            #rRect = oRect.copy()
            #rRect.center = self.image.get_rect().center
            #rImage = rImage.subsurface(rRect).copy()
            #self.image = rImage
    def update(self, dT=0):
            #c = self.image.get_rect().center
            self.image = pygame.transform.rotate(self.origImage,self.rotate)
            #self.image.get_rect().center = c
            self.rotate += 90
            if self.rotate > 360:
                self.rotate = 0
            self.pos = self.mouse_pos
