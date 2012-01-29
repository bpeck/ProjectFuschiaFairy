""" main.py   
Setting up the basic functions & variables 
used by multiple modules
by Adam Rickert, 2011 
"""

import pygame, os, random

#pygame.locals import * causes pygame to include only the constants from the imported modules
from pygame.locals import *

from gamelib.Menu import Menu

def main():
    random.seed()

    #centers the pygame window in the middle of the monitor - HANDY :)
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    
    #can pre-set the mixer init arguments: pre_init(frequency=0, size=0, stereo=0, buffer=0) 
    #pygame.mixer.pre_init(44100, -16, 2, 4096)
    
    pygame.init()
    #pygame.mouse.set_visible(0)
    #set the program icon on the pygame window to my own custom sprite
    #pygame.display.set_icon(pygame.image.load(data.filepath("bowser1.gif")))
    pygame.display.set_caption("GGJ 2012 - Fuschia Fairies")
    screen = pygame.display.set_mode((640, 480))#, pygame.FULLSCREEN)
    
    #starts the "Menu" state of the game to let the player choose options
    Menu(screen)
