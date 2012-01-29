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
        self.dieImg = [pygame.image.load('data/Predator 01.png'),     
        pygame.image.load('data/Predator 02.png'),
        pygame.image.load('data/Predator 03.png'),
        pygame.image.load('data/Predator 04.png'),
        pygame.image.load('data/Predator 05.png'),
        pygame.image.load('data/Predator 06.png'),
        pygame.image.load('data/Predator 07.png'),     
        pygame.image.load('data/Predator 08.png'),
        pygame.image.load('data/Predator 09.png')]
        self.dieLvl = 0
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
        cImg = self.origImage
        if time.time() - self.birth > Variables.PredatorLS:

            if self.dieLvl == len(self.dieImg)-1:
                self.iDied = 1
            else:
                self.dieLvl += 1
            print self.dieLvl
            cImg = self.dieImg[self.dieLvl]
            
        NPC.update(self, dT)
        self.rotate += 7.5
        if self.rotate >= 345:
            self.rotate = 0
        old = Vect2(self.image.get_rect().center)
        rot_image = pygame.transform.rotate(cImg, self.rotate)
        self.image = rot_image
        new = Vect2(rot_image.get_rect().center)
        self.pos = self.pos-(new-old)
        self.lifeSpan -= dT
        if self.lifeSpan < 0:
            self.lifeSpan = 10000

            #begin death animation
            x =1
        if not self.grabbedBy:
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
        else:
            self.pos = self.grabbedBy.pos

