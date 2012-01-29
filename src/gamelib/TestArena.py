import random, math

import pygame

from Arena import Arena
from CircleGuy import CircleGuy
from MouseEntity import MouseEntity
from Predator import Predator
from Prey import Prey

import Variables as Variables
from Variables import *

class TestArena(Arena):
    

    def __init__(self, screen, currentLevel):
        Arena.__init__(self)
        

        self.entities = []
        self.keyListeners = []
        self.accelerators = []
        self.npcs = []
        
        # on a timer, we reset which npc emit attractive and repulsive forces
        self.foodieAcceleratorReset = 5000 # ms
        # this counter is incremented and reset on each repopulation
        self.foodieAcceleratorResetTimer = 0
        # we roll an n sided die for each Foodie to decide whether it will 
        # become an accelerator on this reset
        self.foodieAcceleratorResetDice = 5
    
        # init npcs
        
        maxSize = 50.0
        minSize = 6.0
        
        screenW = float(screen.get_width())
        screenH = float(screen.get_height())
        
        # rotation accel rates
        maxRotVel = math.pi / 20.0
        maxRotAcc = math.pi / 40.0

        for i in range(Variables.lvlFoodCount[currentLevel]):
            size = minSize + random.random() * (maxSize - minSize)
            pos = [0.0,0.0]
            pos[0] += int(random.random() * screenW)
            pos[1] += int(random.random() * screenH)            
            prey = Prey(size, pos, maxRotVel, maxRotAcc, self)

            self.entities.append(prey)

        for i in range(Variables.lvlEaterCount[currentLevel]):
            size = minSize + random.random() * (maxSize - minSize)
            pos = [0.0,0.0]
            pos[0] += int(random.random() * screenW)
            pos[1] += int(random.random() * screenH)
            predator = Predator(size, pos, maxRotVel, maxRotAcc, self)
            
            self.entities.append(predator)
        
        # init players
        c = CircleGuy(self)
        m = MouseEntity(self)
        self.accelerators += [m]
        self.entities += [c, m]

        
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
