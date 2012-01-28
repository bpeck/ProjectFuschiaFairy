from pygame.rect import Rect
from pygame import Surface
from pygame import draw
from InputListener import InputListener


class CircleGuy(Entity, InputListener):
    
    def __init__(self):
        self.name = 'CircleGuy'
        self.pos = (0.0, 0.0)
        self.rect = Rect(0,0,50,50)
        
        self.image = Surface(rect)
        draw.circle(image, (255,255,255), rect.center, rect.w, width=2)

    
    def processEvent(event, dT):
        if event.type == KEYDOWN:
            if event.key == pygame.K_w:
                self.pos[1] += 1.0
            if event.key == pygame.K_a:
                self.pos[0] += -1.0
            if event.key == pygame.K_s:
                self.pos[1] += -1.0
            if event.key == pygame.K_d:
                self.pos[0] += 1.0
    
    
