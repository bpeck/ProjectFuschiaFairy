from pygame import Surface, Sprite

class Entity(object, Sprite):

    def __init__(self):
        self.rect = None
        self.image = None
        
        self.pos = (0.0, 0.0)
    
    def render(self, screen, dT=0.0):
        Surface.blit(self.image, screen, (int(self.pos[0]), int(self.pos[1])))
    
    def getPos(self):
        return self.pos
    
    def px(self):
        return self.pos[0]
    
    def py(self):
        return self.pos[1]
