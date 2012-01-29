""" variables.py   

"""

#! /usr/bin/env python

import pygame

currentPreyCount = 0
currentPredatorCount = 0
#food/eater counts per level 
lvlFoodCount = [0,0,0,0]
lvlEaterCount = [0,0,0,0]
#lvl 1
lvlFoodCount[0] = 3
lvlEaterCount[0] =2
#lvl 2
lvlFoodCount[1] = 4
lvlEaterCount[1] = 3
#lvl 3 
lvlFoodCount[2] = 4
lvlEaterCount[2] = 4
#lvl 4
lvlFoodCount[3] = 5
lvlEaterCount[3] = 6

#LifeSpans in seconds, maybe mod by level
PredatorLS = 3
KeyplayerLS = 30



#KEYS
#Set up the key controls for the game
#KEYS
#Set up the key controls for the game
escapeKey = pygame.K_ESCAPE
downKey = pygame.K_DOWN
upKey = pygame.K_UP
returnKey = pygame.K_RETURN
spaceKey = pygame.K_SPACE

leftKey = pygame.K_a
rightKey = pygame.K_d
jumpKey = pygame.K_SPACE

