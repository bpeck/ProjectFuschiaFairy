import random

import pygame

from Arena import Arena
from CircleGuy import CircleGuy
from MouseEntity import MouseEntity
from Foodie import Foodie

class TestArena(Arena):
    
    def __init__(self, screen):
        self.entities = []
        self.keyListeners = []
    
        # init foodies
        
        maxSize = 40.0
        minSize = 5.0
        
        screenW = float(screen.get_width())
        screenH = float(screen.get_height())
        
        for i in range(40):
            size = minSize + random.random() * (maxSize - minSize)
            pos = [0.0,0.0]
            pos[0] += int(random.random() * screenW)
            pos[1] += int(random.random() * screenH)
            color = pygame.Color(255,0,0)
            hslaC = color.hsla
            color.hsla = (int(random.random() * 360.0), hslaC[1], hslaC[2], hslaC[3])
            foodie = Foodie(size, color, pos)
            
            self.entities.append(foodie)
        
        # init players
        c = CircleGuy()
        m = MouseEntity()
        self.entities += [c, m]
        self.keyListeners += [c, m]
    
    def getInitialEntities(self):
        return self.entities
    
    def getInitialKeyListeners(self):
        return self.keyListeners
