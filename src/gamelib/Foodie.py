import random
import math

import pygame
from pygame.rect import Rect
from pygame import Surface
from pygame import draw

from Entity import Entity
from InputListener import InputListener
from Accelerator import Accelerator
from Vect2 import Vect2
from Util import clamp, clampAmp


class Foodie(Entity):
    
    WANDER, GOALPT, CHASE, RUN, NUMBEHAVIORS = range(5)
    
    def __init__(self, size, color, position, maxRotVel, maxRotAcc):
        Entity.__init__(self)
        
        self.name = 'CircleGuy'
        self.color = color
        
        self.rot = 0 # radians
        self.rotVel = 0.0
        self.rotAcc = 0.0
        
        self.maxRotVel = maxRotVel
        self.maxRotAcc = maxRotAcc
        
        self.pos = Vect2(position)
        self.vel = Vect2([0.0, 0.0])
        self.acc = Vect2([0.5, 0.0])
        self.maxSpeed = 3.25
        
        self.rect = Rect(0,0,size,size)
        self.radius = size/2
        self.image = Surface(self.rect[2:])
        self.image.set_colorkey((0,0,0))
        self.image.lock()
        draw.circle(self.image, self.color, self.rect.center, self.rect.w/2, 1)
        self.image.unlock()
        self.radius = float(size) / 2.0
        
        self.goalPt = Vect2([320.0, 240.0])
        self.behavior = Foodie.WANDER
        self.behaviorCounter = 1000
    
    def collide(self, dT):
        collision = self.arena.collisions[self]
        if collision != None:
            other, dist = collision
            if dist > 0.0:
                bounceAngle = (self.pos - other.pos).perp().normalize(1.0)
            else:
                bounceAngle = Vect2([0.5, 0.5])
            if self.pos[0] > other.pos[0]:
                bounceAngle *= -1.0
            
            self.vel = bounceAngle * self.vel.magnitude()
    
    # behavior that is called in update
    def goTowardsPt(self, dT):
        pass
    
    
    def wander(self, dT):
        # update the rotation acc by random amount
        self.rotAcc = clampAmp(-self.maxRotAcc + \
            self.rotAcc + \
            (random.random() * self.maxRotAcc * 2.0), \
            self.maxRotAcc)
        
        # update the rotation vel by rotAcc
        self.rotVel = clampAmp(self.rotVel + self.rotAcc, self.maxRotVel)
        
        self.rot += self.rotVel
        
        # update linear acc based on current rotation direction
        self.acc[0] = math.cos(self.rot) * 2.0
        self.acc[1] = math.sin(self.rot) * 2.0
    
    
    def runTowardsClosestEntity(self, dT):
        pass
    
    def update(self, dT):
        self.behaviorCounter -= dT
        
        if self.behavior == Foodie.WANDER:
            self.wander(dT)
            if self.behaviorCounter < 0:
                self.behavior = Foodie.WANDER
                self.behaviorCounter = 3000
        elif self.behavior == Foodie.GOALPT:
            self.goTowardsPt(dT)
        
        Entity.move(self)
        
        self.collide(dT)
        
        halfW = int(float(self.rect.w) / 2.0)
        if self.pos[0] + halfW > 640:
            self.pos[0] = 0
            self.vel[0] *= 2.0
        if self.pos[0] + halfW < 0:
            self.pos[0] = 640
            self.vel[0] *=2.0
        halfH = int(float(self.rect.h) / 2.0)
        if self.pos[1] + halfH > 480:
            self.pos[1] = 0
            self.vel[1] *= 2.0
        if self.pos[1] + halfH < 0:
            self.pos[1] = 480
            self.vel[1] *= 2.0
        
