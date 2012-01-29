import pygame
from pygame.rect import Rect
from pygame import Surface
from pygame import draw

from Entity import Entity
from InputListener import InputListener
from Vect2 import Vect2

class CircleGuy(Entity, InputListener):
    
    def __init__(self):
        Entity.__init__(self)
        self.name = 'CircleGuy'
        self.pos = Vect2((100.0, 100.0))

       # self.rect = Rect(0,0,50,50)
        
        self.keys = [False]*512
        
        self.image = pygame.image.load("data/keyPlayer.png")
        self.radius = self.image.get_rect().width/2
       # self.image.set_colorkey((0,0,0))
      #  self.image.lock()
       # draw.circle(self.image, (255,0,0), self.rect.center, self.rect.w/2, 1)
        #self.image.unlock()

        
        self.speed = 1.5
        self.maxSpeed = 5.0
        self.drag  = 0.95
        
        self.radius = float(self.image.get_width()) / 2.0
    
    def processEvent(self, event, dT=0):
        if event.type == pygame.KEYDOWN:
            self.keyDown(event.key)
        if event.type == pygame.KEYUP:
            self.keyUp(event.key)

    def keyDown(self, k):
        self.keys[k] = True
        
    def keyUp(self, k):
        self.keys[k] = False
    
    def collide(self, entity):
        pass
        #print "touched by an uncle"
    
    def update(self,DT):
        self.acc = Vect2([0, 0])
        if self.keys[pygame.K_w]: self.acc[1] -= self.speed
        if self.keys[pygame.K_a]: self.acc[0] -= self.speed
        if self.keys[pygame.K_s]: self.acc[1] += self.speed
        if self.keys[pygame.K_d]: self.acc[0] += self.speed

        self.move()
        
		# wrap around the playfield
        if self.pos[0] > 640: self.pos[0] = 0
        if self.pos[0] < 0:   self.pos[0] = 640
        if self.pos[1] > 480: self.pos[1] = 0
        if self.pos[1] < 0:   self.pos[1] = 480
