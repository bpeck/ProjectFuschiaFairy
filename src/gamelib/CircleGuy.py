import pygame
from pygame.rect import Rect
from pygame import Surface
from pygame import draw

from Actor import Actor
from InputListener import InputListener
from Vect2 import Vect2

class CircleGuy(Actor, InputListener):
    
    def __init__(self):
        Actor.__init__(self, 0.5)
        self.name = 'CircleGuy'
        self.pos = Vect2((100.0, 100.0))
        self.rect = Rect(0,0,50,50)
        
        self.image = Surface(self.rect[2:])
        self.image.set_colorkey((0,0,0))
        self.image.lock()
        draw.circle(self.image, (255,0,0), self.rect.center, self.rect.w/2, 1)
        self.image.unlock()
    
    def processEvent(self, event, dT=0):
        if event.type == pygame.KEYDOWN:
            self.keyDown(event.key)
        if event.type == pygame.KEYUP:
            self.keyUp(event.key)
