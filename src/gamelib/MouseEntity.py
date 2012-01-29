import pygame, math
from pygame.rect import Rect
from pygame import Surface
from pygame import draw

from Entity import Entity
from InputListener import InputListener
from NPC import NPC
from Data import *
from Vect2 import Vect2

class MouseEntity(InputListener, Entity):

    def __init__(self):
        Entity.__init__(self)
        self.name = 'MouseEntity'
        self.mouse_pos = Vect2([0.0, 0.0])
        self.origImage = pygame.image.load('data/mousePlayer.png')
        self.image =  self.origImage
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
        self.grabDist = 12 # pixel distance within which you can grab something
        self.grabbedEntity = None
        
    def processEvent(self, event, dT=0):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.imgState = 1
            closest_entity, dist = self.arena.closest[self]
            if isinstance(closest_entity, Prey) and dist <= self.grabDist:
                self.grab(closest_entity)  
            else:
                print str(dist) + " pixels away"
        elif event.type == pygame.MOUSEMOTION:
            # center the position at the mouse
            oldPos = self.mouse_pos
            self.mouse_pos = Vect2(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            self.imgState = 0
            self.image = self.origImage
            if self.grabbedEntity:
                self.release()
            
            
    def biteAnim(self):
        if self.imgState == 1:
            self.image = self.image1
            self.imgState += 1
        if self.imgState == 2:
            self.image = self.image2
            self.imgState += 1
        if self.imgState == 3:
            self.image = self.image3
 
    def grab(self, entity):
        entity.grabbedBy = self
        self.grabbedEntity = entity
        self.grabbing = True
    
    def release(self):
        self.grabbedEntity.grabbedBy = None
        self.grabbedEntity.maxSpeed = 20.0
        self.grabbedEntity.acc = self.vel * 3.0
        self.grabbedEntity.behavior = NPC.THROWN
        self.grabbedEntity.behaviorCounter = 700
        self.grabbedEntity = None
            
    def update(self, dT=0):
            if self.imgState > 0:
                self.biteAnim()

            self.vel = (self.mouse_pos-self.pos)/5.0
                
            self.move()
