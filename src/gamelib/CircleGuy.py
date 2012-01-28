import pygame
from pygame.rect import Rect
from pygame import Surface
from pygame import draw

from Entity import Entity
from InputListener import InputListener


class CircleGuy(Entity, InputListener):
    
    def __init__(self):
        self.name = 'CircleGuy'
        self.pos = [100.0, 100.0]
        self.rect = Rect(0,0,50,50)
        
        self.image = Surface(self.rect[2:])
        self.image.lock()
        self.image.fill((255, 255, 255))
        #draw.circle(self.image, (255,255,255), self.rect.center, self.rect.w, 4)
        self.image.unlock()
    
    def processEvent(self, event, dT):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.pos[1] += 1.0
            if event.key == pygame.K_a:
                self.pos[0] += -1.0
            if event.key == pygame.K_s:
                self.pos[1] += -1.0
            if event.key == pygame.K_d:
                self.pos[0] += 1.0
    
    
