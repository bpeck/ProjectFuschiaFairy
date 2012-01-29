from pygame import Surface
from pygame.sprite import Sprite

from Vect2 import Vect2

class Entity(Sprite):

    def __init__(self):
        self.rect = None
        self.image = None
        
        self.pos = Vect2([0.0, 0.0])
        self.vel = Vect2([0.0, 0.0])
        self.acc = Vect2([0.0, 0.0])

        self.maxSpeed = 1.0
        self.drag = 1.0
        
        self.radius = 0
        self.collides = True
        
        self.entity = None
    
    def update(self, dT=0.0):
        self.move()
    
    def move(self, dT=0.0):
        self.vel += self.acc
        if self.vel.magnitude() > self.maxSpeed:
          self.vel = self.vel.normalize(self.maxSpeed)
        self.vel *= self.drag
        self.pos += self.vel
        
    def displace(self, entity, distance):
        if distance > self.radius+entity.radius: return
        impact_normal = (self.pos - entity.pos).normalize()
        overlap = distance - (self.radius+entity.radius)
        self.pos = self.pos - impact_normal*overlap

#        var a1:Number =   velocity.dot(impact_normal);
#        var a2:Number = a.velocity.dot(impact_normal);
#        var p:Number = (2.0 * (a1 - a2)) / (mass + a.mass);
#        velocity   =   velocity.subtract(impact_normal.multiply(p*a.mass));
#        a.velocity = a.velocity.add     (impact_normal.multiply(p*  mass));
    
    def collide(self, entity):
        pass
    
    def render(self, screen, dT=0.0):
        screen.blit(self.image, (int(self.pos[0]-self.radius), int(self.pos[1]-self.radius)))
    
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
