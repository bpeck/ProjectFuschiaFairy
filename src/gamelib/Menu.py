""" menu.py   
Setting up the different menu states which
the player can use to operate the game
by Adam Rickert, 2011 
"""

#! /usr/bin/env python

import pygame, sys
from pygame.locals import *

import Variables as variables
from Variables import *

from Game import Game

from Data import *


def RunGame(screen): #defining the various game states
    Game(screen)
    #play_music(audio.titleTheme, 0.50)
    
def ContinueGame(screen):
    Game(screen, True)
    #play_music(audio.titleTheme, 0.50)
               
def Help(screen):
    menuScreen = MenuTransition(screen, ["HELP",
    "",
    "Move: A and D Keys",
    "Jump: Space Bar",
    "Shoot LAZAH!: L Mouse Button",
    "Return: Esc = return",
    "Note: Shoot enemies to kill them!",
    ""])

def MenuTransition(screen, text): #define the classes that make up the menu's for the game
    
    font = pygame.font.Font(filepath("fonts/font.ttf"), 16)
    black = pygame.Surface((640, 480))
    black.fill((0, 0, 0))
    alpha = 255
    
    intro = True
    outro = False
    
    height = len(text)*(font.get_height()+3)
    image = pygame.Surface((640, height))
    
    y = 0
    for line in text:
        ren = font.render(line, 1, (255, 255, 255))
        image.blit(ren, (320-ren.get_width()/2, y*(font.get_height()+3)))
        y += 1
    while 1:
        pygame.time.wait(10)
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
            if e.type == KEYDOWN:
                if e.key == variables.escapeKey:
                    return
                if e.key in (variables.spaceKey, variables.returnKey):
                    intro = False
                    outro = True
        if intro:
            if alpha > 0:
                alpha -= 5
        if outro:
            if alpha < 255:
                alpha += 5
            else:
                return
        black.set_alpha(alpha)
        screen.fill((0, 0, 0))
        screen.blit(image, (0, 240-image.get_height()/2))
        screen.blit(black, (0, 0))
        ren = font.render("Press Enter to continue", 1, (255, 255, 255))
        screen.blit(ren, (320-ren.get_width()/2, 460))
        pygame.display.flip()

class MenuSetup:

    def __init__(self, *options):

        self.options = options
        self.x = 0
        self.y = 0
        self.font = pygame.font.Font(pygame.font.match_font("Verdana"), 32)
        self.option = 0
        self.width = 1
        self.color = [0, 0, 0]
        self.hcolor = [255, 0, 0]
        self.height = len(self.options)*self.font.get_height()
        for o in self.options:
            text = o[0]
            ren = self.font.render(text, 1, (0, 0, 0))
            if ren.get_width() > self.width:
                self.width = ren.get_width()

    def draw(self, surface):
        i=0
        for o in self.options:
            if i==self.option:
                clr = self.hcolor
            else:
                clr = self.color
            text = o[0]
            ren = self.font.render(text, 1, clr)
            if ren.get_width() > self.width:
                self.width = ren.get_width()
            surface.blit(ren, ((self.x+self.width/2) - ren.get_width()/2, self.y + i*(self.font.get_height()+4)))
            i+=1
            
    def update(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == variables.downKey:
                    self.option += 1
                if e.key == variables.upKey:
                    self.option -= 1
                if e.key == variables.returnKey:
                    self.options[self.option][1]()
        if self.option > len(self.options)-1:
            self.option = 0
        if self.option < 0:
            self.option = len(self.options)-1

    def set_pos(self, x, y):     
        self.x = x
        self.y = y
        
    def set_font(self, font):
        self.font = font
        
    def set_highlight_color(self, color):
        self.hcolor = color
        
    def set_normal_color(self, color):
        self.color = color
        
    def center_at(self, x, y):
        self.x = x-(self.width/2)
        self.y = y-(self.height/2)

class Menu():    

    def __init__(self, screen):
        self.screen = screen
        self.menu = MenuSetup(["", lambda: RunGame(screen)]
                              #, ["HELP", lambda: Help(screen)]
                              #, ["Exit", sys.exit]
                              )
        
        self.menu.set_highlight_color((255, 0, 0))
        self.menu.set_normal_color((255, 255, 255))
        
        self.menu.center_at(300, 400)
        self.bg = pygame.image.load('data/Background-640-Lev1.png')
        self.bgOverlay = pygame.image.load('data/Title.png')
        
        #self.menu.set_font(pygame.font.Font(filepath("fonts/tandelle regular.ttf"), 16))
        
        #play_music(audio.titleTheme, 0.50, 1)
        
        self.clock = pygame.time.Clock()
        events = pygame.event.get()
        self.menu.update(events)
        self.menu.draw(self.screen)
        self.main_loop()
  
    def main_loop(self):
        while 1:
            self.clock.tick(60)
            events = pygame.event.get()
            self.menu.update(events)
            for e in events:
                if e.type == QUIT:
                    pygame.quit()
                    return
                if e.type == KEYDOWN and e.key == variables.escapeKey:
                    pygame.quit()
                    return
                
            self.screen.blit(self.bg, (0, 0))
            self.screen.blit(self.bgOverlay, (0, 0))
            
            self.menu.draw(self.screen)
            pygame.display.flip()
            
