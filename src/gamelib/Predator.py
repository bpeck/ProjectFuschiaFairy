from NPC import NPC

import pygame

class Predator(NPC):
    
    def __init__(self, size, position, maxRotVel, maxRotAcc):
        NPC.__init__(self, size, position, maxRotVel, maxRotAcc)
        self.origImage = pygame.image.load('data/Predator.png')      
        self.image = self.origImage 
        self.name = 'Predator'
        self.lifeSpan = 10000
    
    def update(self, dT):
        NPC.update(self, dT)
        self.lifeSpan -= dT
        if self.lifeSpan < 0:
            self.lifeSpan = 10000
