import pygame
from pygame.rect import Rect
from pygame import Surface
from pygame import draw
from Entity import Entity

class Actor(Entity):

    def __init__(self, baseSpeed):
        self.keys = [False]*128
        self.baseSpeed = baseSpeed
        self.xMod = 0
        self.yMod = 0
        self.maxSpeedX = 3
        self.maxSpeedY = 3
        self.minSpeedX = -3.0 
        self.minSpeedY = -3.0 
    
    def keyDown(self, k):
        self.keys[k] = True
    def keyUp(self, k):
        self.keys[k] = False
    
    def update(self,DT):
        if self.keys[pygame.K_w] and self.yMod > self.minSpeedY:
            #self.kd = 'w'
            self.yMod += -1.0 * self.baseSpeed
        if self.keys[pygame.K_a] and self.xMod > self.minSpeedX:
            #self.kd = 'a'
            self.xMod += -1.0 * self.baseSpeed
        if self.keys[pygame.K_s] and self.yMod < self.maxSpeedY:
            #self.kd = 's'
            self.yMod += self.baseSpeed
        if self.keys[pygame.K_d] and self.xMod < self.maxSpeedX:
            #self.kd = 'd'
            self.xMod += self.baseSpeed

        if self.yMod > 0:
            self.yMod -= .05
        if self.yMod < 0:
            self.yMod += .05

#	if self.kd != 'a' or self.kd != 'd':
        if self.xMod > 0:
            self.xMod -= .05
        if self.xMod < 0:
            self.xMod += .05

        if self.pos[0] > 640:
            self.pos[0] = 0
        if self.pos[0] < 0:
            self.pos[0] = 640
        if self.pos[1] > 480:
            self.pos[1] = 0
        if self.pos[1] < 0:
            self.pos[1] = 480

#        print 'xMod: ' + str(self.xMod)
#        print 'yMod: ' + str(self.yMod)
        self.pos[0] += self.xMod
        self.pos[1] += self.yMod
