from NPC import NPC
import pygame

class Prey(NPC):
    
    def __init__(self, size, position, maxRotVel, maxRotAcc, a):
       
        NPC.__init__(self, size, position, maxRotVel, maxRotAcc, a)
        
        self.name = 'Prey'
        self.alive = True
        self.deathAnim = []
        for i in range(6):
            self.deathAnim.append( pygame.image.load('data/Prey 0%d.png' % (i+1)))
        self.imageIndex = 0
        self.image = self.deathAnim[self.imageIndex]
        self.radius = self.image.get_rect().width/2
        self.lifeSpan = 30 * len(self.deathAnim)
        
    def collide(self):
        for collision in self.arena.collisions[self]:
            entity, dist = collision
            if entity.name == 'Predator':
                self.iDied = 1
            
            if entity.name == 'Prey':
                self.displace(entity, dist)
    
    def update(self, dT):
        if not self.grabbedBy:
            self.collide()
            NPC.update(self, dT)
        else:
            self.pos = self.grabbedBy.pos
        
        if not self.alive:
            self.imageIndex += 1
            self.image = self.deathAnim[min(self.imageIndex, len(self.deathAnim)-1)]
