import random

import pygame

from Arena import Arena
from CircleGuy import CircleGuy
from MouseEntity import MouseEntity
from Foodie import Foodie
from Eater import Eater

import Variables as Variables
from Variables import *

class TestArena(Arena):
    
    def __init__(self, screen, currentLevel):
        self.entities = []
        self.keyListeners = []
    
        # init foodies
        
        maxSize = 40.0
        minSize = 5.0
        
        screenW = float(screen.get_width())
        screenH = float(screen.get_height())
        
        for i in range(Variables.lvlFoodCount[currentLevel]):
            size = minSize + random.random() * (maxSize - minSize)
            pos = [0.0,0.0]
            pos[0] += int(random.random() * screenW)
            pos[1] += int(random.random() * screenH)
            foodie = Foodie(size, pos)
            self.entities.append(foodie)

        for i in range(Variables.lvlEaterCount[currentLevel]):
            size = minSize + random.random() * (maxSize - minSize)
            pos = [0.0,0.0]
            pos[0] += int(random.random() * screenW)
            pos[1] += int(random.random() * screenH)
            pos[0] += int(random.random() * screenW)
            eater = Eater(size, pos)
            self.entities.append(eater)
            
        
        # init players
        c = CircleGuy()
        m = MouseEntity()
        self.entities += [c, m]
        self.keyListeners += [c, m]
    
    def getInitialEntities(self):
        return self.entities
    
    def getInitialKeyListeners(self):
        return self.keyListeners
