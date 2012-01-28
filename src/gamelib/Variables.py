""" variables.py   
Putting the main variables into one file.
by Adam Rickert, 2011 
"""

#! /usr/bin/env python

import pygame

playerJumpHeight = -10
playerHealth = 3
playerLives = 3

walkSpeed = 1.4

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

#leftKey = pygame.K_LEFT
#rightKey = pygame.K_RIGHT
#jumpKey = pygame.K_z
