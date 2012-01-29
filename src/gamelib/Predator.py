from NPC import NPC
from Vect2 import Vect2
import pygame, time
import Variables

import Variables as Variables
from Variables import *


class Predator(NPC):
    
    def __init__(self, size, position, maxRotVel, maxRotAcc):
        NPC.__init__(self, size, position, maxRotVel, maxRotAcc)
        self.origImage = pygame.image.load('data/Predator.png')      
        self.image = self.origImage 
        self.name = 'Predator'
        self.lifeSpan = 10000
        self.birth = time.time()
        self.rotate = 0.0
        self.radius = self.image.get_rect().width/2
    
    def update(self, dT):
        for entity, dist in self.arena.collisions[self]:
            if isinstance(entity, Predator): self.displace(entity, dist)
        #slow die
        if time.time() - self.birth > Variables.PredatorLS:
            #begin death animation
            x =1
        NPC.update(self, dT)
        self.rotate += 7.5
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
