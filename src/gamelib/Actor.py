import pygame
from pygame.rect import Rect
from pygame import Surface
from pygame import draw
from Entity import Entity
from Vect2 import Vect2

class Actor(Entity):

    def __init__(self, baseSpeed):
        self.keys = [False]*128
        self.baseSpeed = baseSpeed
        self.velocity = Vect2((0, 0))
        self.maxSpeed = 3

    def keyDown(self, k):
        self.keys[k] = True
    def keyUp(self, k):
        self.keys[k] = False
    
    def update(self,DT):
	self.pos[0] += 1.0
	return 
        if self.keys[pygame.K_w]:
            self.velocity[1] += -self.baseSpeed
        if self.keys[pygame.K_a]:
            self.velocity[0] += -self.baseSpeed
        if self.keys[pygame.K_s]:
            self.velocity[1] += self.baseSpeed
        if self.keys[pygame.K_d]:
            self.velocity[0] += self.baseSpeed
#        if self.velocity.magnitude() > self.maxSpeed:
#          self.velocity = self.velocity.normalize(self.maxSpeed)

        #self.velocity *= 0.999
        self.pos += self.velocity
        #print self.velocity
        if self.pos[0] > 640:
            self.pos[0] = 0
        if self.pos[0] < 0:
            self.pos[0] = 640
        if self.pos[1] > 480:
            self.pos[1] = 0
        if self.pos[1] < 0:
            self.pos[1] = 480
"""        if self.yMod > 0:
            self.yMod -= .05
        if self.yMod < 0:
            self.yMod += .05

#	if self.kd != 'a' or self.kd != 'd':
        if self.xMod > 0:
            self.xMod -= .05
        if self.xMod < 0:
            self.xMod += .05

"""


