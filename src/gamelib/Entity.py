from pygame import Surface
from pygame.sprite import Sprite

class Entity(Sprite):

    def __init__(self):
        self.rect = None
        self.image = None
        
        self.pos = [0.0, 0.0]
    
    def render(self, screen, dT=0.0):
        screen.blit(self.image, (int(self.pos[0]), int(self.pos[1])))
    
    def getPos(self):
        return self.pos
    
    def px(self):
        return self.pos[0]
    
    def py(self):
        return self.pos[1]
        
    def setpx(self, x):
        self.pos[0] = x
    
    def setpy(self, y):
        self.pos[1] = y
        
    def setPos(self, pos):
        self.pos = pos
