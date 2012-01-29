""" data.py   
Telling pygame where to find all the files
and what to do with them when they're found
by Adam Rickert, 2011 
"""

import os, pygame
from pygame.locals import *

#setting global variables
data_py = os.path.abspath(os.path.dirname(__file__))
data_dir = os.path.normpath(os.path.join(data_py, '..', 'data'))

#defining classes
def filepath(filename):
    return os.path.join(data_dir, filename)

#mode='rb' means that it's reading the file as binary rather than text
def load(filename, mode='rb'):
    return open(os.path.join(data_dir, filename), mode)

def load_image(filename):
    filename = filepath(filename)
    try:
        image = pygame.image.load(filename)
    except pygame.error:
        raise SystemExit, "Unable to load: " + filename
    return image.convert_alpha()

def load_sound(filename, volume=0.5):
    filename = filepath(filename)
    try:
        sound = pygame.mixer.Sound(filename)
        sound.set_volume(volume)
    except:
        raise SystemExit, "Unable to load: " + filename
    return sound

def play_music(filename, volume=0.25, loop=-1):
    filename = filepath(filename)
    try:
        pygame.mixer.music.load(filename)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(loop)
    except:
        raise SystemExit, "Unable to load: " + filename

def stop_music():
    pygame.mixer.music.stop()
