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

        self.image = self.origImage
        self.radius = self.image.get_rect().width/2
        print self.radius
        self.rotate = 45


        self.radius = float(self.image.get_width()) / 2.0

        self.maxSpeed = 30
        
        self.grabbing = False
        self.grabbed_entity = None
        
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
            #c = self.image.get_rect().center
            #self.image = pygame.transform.rotate(self.origImage,self.rotate)
            #self.image.get_rect().center = c
            #self.rotate += 3
            #if self.rotate > 360: self.rotate -= 360
                
            #smoothing 
            self.vel = (self.mouse_pos-self.pos)/10
            self.move()
            
            if self.grabbing and not self.grabbed_entity:
                closest = None
                closest_distance = 0
                for e in self.arena.entities:
                    if e == self: continue
                    distance = e.pos.distance_squared(self.pos)
                    if not closest or distance < closest_distance:
                        closest = e
                        closest_distance = distance
                self.grabbed_entity = closest
            if not self.grabbing and self.grabbed_entity:
                self.grabbed_entity.vel = self.vel
                self.grabbed_entity = None
            if self.grabbed_entity:
                print self.grabbed_entity.pos
                self.grabbed_entity.pos = self.pos
