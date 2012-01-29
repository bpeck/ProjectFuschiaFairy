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


class NPC(Entity):
    
    THROWN, WANDER, GOAL, NUM_NPC_BEHAVIORS = range(4)

    def __init__(self, size, position, maxRotVel, maxRotAcc):
        Entity.__init__(self)
        
        self.name = 'NPC'

        self.rotate = 0
        self.rot = 0 # radians
        self.rotVel = 0.0
        self.rotAcc = 0.0
        
        self.maxRotVel = maxRotVel
        self.maxRotAcc = maxRotAcc
        self.oldPos = Vect2([0.0, 0.0])
        self.pos = Vect2(position)
        self.vel = Vect2([0.0, 0.0])
        self.acc = Vect2([0.5, 0.0])
        self.maxSpeed = 3.25
        
        self.rect = Rect(0,0,size,size)
        self.origImage = pygame.image.load('data/Prey-02.png')      
        self.image = self.origImage 
        self.radius = float(self.origImage.get_width()) / 2.0
        
        self.grabbedBy = None
        
        self.goal = Vect2([320.0, 240.0]) # cn be Vect2 or Entity
        self.forceGoal = False # won't stop going towards goal until it gets there
        self.behavior = NPC.WANDER
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
    def goTowardsGoal(self, dT):
        if isinstance(self.goal, Vect2):
            goalDir = self.goal - self.pos
        else: # assume it's an entity then
            goalDir = self.goal.pos - self.pos
        dist = goalDir.magnitude()
            
        # return true if we reached goal
        if dist < 2.0:
            return True
        goalDir.normalize(1.0)
        # otherwise accelerate towards goal
        self.acc[0] = goalDir[0] * 2.0
        self.acc[1] = goalDir[1] * 2.0
        return False
    
    # behavior that is called in update
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
        
        if self.behavior == NPC.WANDER:
            self.wander(dT)
            if self.behaviorCounter < 0:
                self.behavior = NPC.WANDER
                self.behaviorCounter = 3000
        elif self.behavior == NPC.GOAL:
            atGoal = self.goTowardsGoal(dT)
            if atGoal:
                self.behavior = NPC.WANDER
                self.behaviorCounter = 500
            # if counter expires either keep chasing goal or start wandering
            if self.behaviorCounter < 0:
                if self.forceGoal:
                    self.behavior = NPC.GOAL
                    self.behaviorCounter = 2000
                else:
                    self.behavior = NPC.WANDER
                    self.behaviorCounter = 2000
        elif self.behavior == NPC.THROWN:
            self.maxSpeed = 20.0
            if self.behaviorCounter < 0:
                self.maxSpeed = 3.25
                self.acc = Vect2([0.0,0.0])
                self.behavior = NPC.WANDER
                self.behaviorCounter = 2000 
            
        Entity.move(self)
        
        self.collide(dT)
        
        halfW = int(float(self.rect.w) / 2.0)
        wrapped = False
        if self.pos[0] + halfW > 640:
            self.pos[0] = 0
            wrapped = True
        if self.pos[0] + halfW < 0:
            self.pos[0] = 640
            wrapped = True
        halfH = int(float(self.rect.h) / 2.0)
        if self.pos[1] + halfH > 480:
            self.pos[1] = 0
            wrapped = True
        if self.pos[1] + halfH < 0:
            self.pos[1] = 480
            wrapped = True
        if wrapped:
            # go towards middle of screen for a bit
            self.goal = Vect2([320.00, 240.0])
            self.forceGoal = False
            self.behaviorCounter = 1500
            self.behavior = NPC.GOAL
        

