from NPC import NPC
from Vect2 import Vect2
import pygame, time
import Variables
from Variables import *

class Predator(NPC):
    
    def __init__(self, size, position, maxRotVel, maxRotAcc, a):
        NPC.__init__(self, size, position, maxRotVel, maxRotAcc, a)
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
        self.chaseDist = 200
    
    def collide(self):
        for collision in self.arena.collisions[self]:
            entity, dist = collision
            if entity.name == 'Prey':
                self.lifeSpan += 2000
                self.birth = time.time()
            if entity.name == 'Predator':
                if dist > 0.0:
                    self.displace(entity, dist)
        
        entity, dist = self.arena.closest[self]
        
        if dist < self.chaseDist and entity.name == 'Prey':
            self.behavior = NPC.GOAL
            self.goal = entity
            self.behaviorCounter = 3000
    
    def update(self, dT):
        
        self.collide()
        
        #slow die
        cImg = self.origImage
        if time.time() - self.birth > Variables.PredatorLS:
            if self.dieLvl == len(self.dieImg)-1:
                self.iDied = 1
            else:
                self.dieLvl += 1

            cImg = self.dieImg[self.dieLvl]
            
        NPC.update(self, dT)
        old = Vect2(self.image.get_rect().center)
        rot_image = pygame.transform.rotate(cImg, self.rotate)
        self.image = rot_image
        new = Vect2(rot_image.get_rect().center)
        self.pos = self.pos-(new-old)
        
        self.rotate += 7.5
        if self.rotate >= 345:
            self.rotate = 0

            #begin death animation
            x =1
        if not self.grabbedBy:
            NPC.update(self, dT)
            
            old = Vect2(self.image.get_rect().center)
            rot_image = pygame.transform.rotate(cImg, self.rotate)
            self.image = rot_image
            new = Vect2(rot_image.get_rect().center)
            self.pos = self.pos-(new-old)

        else:
            self.pos = self.grabbedBy.pos

