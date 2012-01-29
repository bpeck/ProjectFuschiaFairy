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
        self.image = self.origImage
        self.radius = self.image.get_rect().width/2
        print self.radius
        self.rotate = 45
        self.maxSpeed = 30
        
        self.grabbing = False
        self.grabbed_entity = None
        
    def processEvent(self, event, dT=0):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
            self.grabbing = True
        if event.type == pygame.MOUSEBUTTONUP and event.button==1:
            self.grabbing = False
        if event.type == pygame.MOUSEMOTION:
            # center the position at the mouse
            oldPos = self.mouse_pos
            self.mouse_pos = Vect2(event.pos)
            
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