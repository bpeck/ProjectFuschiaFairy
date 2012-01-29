from NPC import NPC
from Vect2 import Vect2
import pygame

class Predator(NPC):
    
    def __init__(self, size, position, maxRotVel, maxRotAcc):
        NPC.__init__(self, size, position, maxRotVel, maxRotAcc)
        self.origImage = pygame.image.load('data/Predator.png')      
        self.image = self.origImage 
        self.name = 'Predator'
        self.lifeSpan = 10000
        self.rotate = 0
    
    def update(self, dT):
        NPC.update(self, dT)
        self.rotate += 15
        if self.rotate >= 345:
            self.rotate = 0
        old = Vect2(self.image.get_rect().center)
        rot_image = pygame.transform.rotate(self.origImage, self.rotate)
        self.image = rot_image
        new = Vect2(rot_image.get_rect().center)
        self.pos = self.pos-(new-old)
        self.lifeSpan -= dT
        if self.lifeSpan < 0:
            self.lifeSpan = 10000
