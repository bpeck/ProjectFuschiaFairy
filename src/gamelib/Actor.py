import pygame
from pygame.rect import Rect
from pygame import Surface
from pygame import draw
from Entity import Entity

class Actor(Entity):

    def __init__(self):
       
        self.baseSpeed = 1.0
        self.xMod = 0
        self.yMod = 0
        self.maxSpeedX = 10.0 * self.baseSpeed
        self.maxSpeedY = 10.0 * self.baseSpeed
        self.minSpeedX = -10.0 * self.baseSpeed
        self.minSpeedY = -10.0 * self.baseSpeed
        print(self.xMod)
    
    def move(self, k):
        if k == pygame.K_w and self.yMod < self.maxSpeedY:
            self.yMod += baseSpeed
        if k == pygame.K_a and self.xMod > self.minSpeedX:
            self.xMod += -1.0 * baseSpeed
        if k == pygame.K_s and self.yMod > self.minSpeedY:
            self.yMod += -1.0 * baseSpeed
        if k == pygame.K_d and self.xMod < self.maxSpeedX:
            self.xMod += baseSpeed

    
    #def update(self,DT):
    #print(self.xMod)
        #self.pos[0] += self.xMod
        #self.pos[1] += self.yMod
