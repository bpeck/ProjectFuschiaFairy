import random, math

import pygame

from Arena import Arena
from CircleGuy import CircleGuy
from MouseEntity import MouseEntity
from Foodie import Foodie

class TestArena(Arena):
    
    def __init__(self, screen):
        Arena.__init__(self)
        
        self.entities = []
        self.keyListeners = []
        self.accelerators = []
        self.foodies = []
        
        # on a timer, we reset which foodies emit attractive and repulsive forces
        self.foodieAcceleratorReset = 5000 # ms
        # this counter is incremented and reset on each repopulation
        self.foodieAcceleratorResetTimer = 0
        # we roll an n sided die for each Foodie to decide whether it will 
        # become an accelerator on this reset
        self.foodieAcceleratorResetDice = 5
    
        # init foodies
        
        maxSize = 50.0
        minSize = 6.0
        
        screenW = float(screen.get_width())
        screenH = float(screen.get_height())
        
        for i in range(40):
            # diameter
            size = minSize + random.random() * (maxSize - minSize)
            
            # initial position
            pos = [0.0,0.0]
            pos[0] += int(random.random() * screenW)
            pos[1] += int(random.random() * screenH)
            
            # color of Foodie
            color = pygame.Color(255,0,0)
            hslaC = color.hsla
            color.hsla = (int(random.random() * 360.0), hslaC[1], hslaC[2], hslaC[3])
            
            # rotation accel rates
            maxRotVel = math.pi / 20.0
            maxRotAcc = math.pi / 40.0
            
            foodie = Foodie(size, color, pos, maxRotVel, maxRotAcc)
            
            self.foodies.append(foodie)
            self.entities.append(foodie)
        
        # init players
        c = CircleGuy()
        m = MouseEntity()
        self.accelerators += [m]
        self.entities += [c, m]
        for e in self.entities:
            e.arena = self
        
        self.keyListeners += [c, m]
    
    def getInitialEntities(self):
        return self.entities
    
    def getInitialKeyListeners(self):
        return self.keyListeners
    
    def update(self, dT):
        Arena.update(self, dT)
        
        '''
        self.foodieAcceleratorResetTimer += dT
        if self.foodieAcceleratorResetTimer > self.foodieAcceleratorReset:
            print "RESETING ACCELERATIN FOODIES"
            # remove all foodies from the accelerators list
            for a in self.accelerators:
                if isinstance(a, Foodie):
                    self.accelerators.remove(a)
            # randomly add some foodies back in
            for f in self.foodies:
                if random.randint(0, self.foodieAcceleratorResetDice) == 0:
                    self.accelerators.append(f)
            self.foodieAcceleratorResetTimer = 0
        '''
        pass                        
