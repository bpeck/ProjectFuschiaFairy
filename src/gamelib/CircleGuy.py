import pygame
from pygame.rect import Rect
from pygame import Surface
from pygame import draw

from Actor import Actor
from InputListener import InputListener
from Vect2 import Vect2

class CircleGuy(Actor, InputListener):
    
    def __init__(self):
        Actor.__init__(self, 1)
        self.name = 'CircleGuy'
        self.pos = Vect2((100.0, 100.0))
        self.rect = Rect(0,0,50,50)
        
        self.image = Surface(self.rect[2:])
        self.image.lock()
        self.image.fill((255, 255, 255))
        #draw.circle(self.image, (255,255,255), self.rect.center, self.rect.w, 4)
        self.image.unlock()
    
    def processEvent(self, event, dT=0):
        if event.type == pygame.KEYDOWN:
            self.keyDown(event.key)
        if event.type == pygame.KEYUP:
            self.keyUp(event.key)
