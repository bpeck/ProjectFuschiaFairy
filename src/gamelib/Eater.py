import random
import math

import pygame
from pygame.rect import Rect
from pygame import Surface
from pygame import draw

from Entity import Entity
from InputListener import InputListener
from Vect2 import Vect2
from Util import clamp, clampAmp


class Eater(Entity):
    
    def __init__(self, size, position, maxRotVel = math.pi / 10.0, maxRotAcc = math.pi / 20.0):
        Entity.__init__(self)
        self.slowdown = 0
        self.name = 'BadGuy'

        self.rotate = 0
        self.rot = 0 # radians
        self.rotVel = 0.0
        self.rotAcc = 0.0
        self.maxRotVel = maxRotVel
        self.maxRotAcc = maxRotAcc
        self.oldPos = Vect2([0.0, 0.0])
        self.pos = Vect2(position)
        self.vel = Vect2([0.25, 0.0])
        self.acc = Vect2([0.0, 0.0])
        self.maxSpeed = 0.5
        
        self.rect = Rect(0,0,size,size)
        self.origImage = pygame.image.load('data/Predator.png')      
        self.image = self.origImage 
        # self.image = Surface(self.rect[2:])
       # self.image.set_colorkey((0,0,0))
       # self.image.lock()
       # draw.circle(self.image, self.color, self.rect.center, self.rect.w/2, 1)
       # self.image.unlock()
    
    def update(self, dT):
       # self.slowdown += 1
        #if self.slowdown % 50 == 0:    
            # update the rotation acc by random amount
            self.rotAcc = clampAmp(-self.maxRotAcc + \
                self.rotAcc + \
                (random.random() * self.maxRotAcc * 2.0), \
                self.maxRotAcc)
            
            # update the rotation vel by rotAcc
            self.rotVel = clampAmp(self.rotVel + self.rotAcc, self.maxRotVel)
            
            self.rot += self.rotVel
            
            # update linear vel based on current rotation direction
            self.vel[0] = math.cos(self.rot) * self.maxSpeed
            self.vel[1] = math.sin(self.rot) * self.maxSpeed
            self.oldPos[0] = self.pos[0] 
            self.oldPos[1] = self.pos[1]
            Entity.move(self)

            self.pos[0] %= 640
            self.pos[1] %= 480
            angle = math.degrees(math.atan2(self.oldPos[0]-self.pos[0], self.oldPos[1]-self.pos[1]))+180
            print angle
            self.image = pygame.transform.rotate(self.origImage, angle)
            
