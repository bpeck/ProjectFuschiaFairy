""" Arena class is in charge of initializing a play-space, and supplying our
Game class with a list of entities to render and update """

class Arena(object):
    
    def __init__(self):
        self.entities = []
        self.keyListeners = []
        self.accelerators = []
        
        self.collisions = {}
        self.closest = {}
    
    def collisionDetect(self, entity, dT = 0.0):
        if not entity.collides:
            return
        self.collisions[entity] = []
        self.closest[entity] = None

        minDist = 99999.0
        
        for other in self.entities:
            if not other.collides or other == entity:
                continue
                
            dist = entity.pos.distance(other.pos)
            if dist < entity.radius+other.radius:
                self.collisions[entity].append((other, dist))
            
            if dist < minDist:
                minDist = dist
                self.closest[entity] = (other, dist)
    
    def doAccelerators(self):
        for a in self.accelerators:
            for e in self.entities:
                a.affectEntity(e)
    
    def getInitialEntities(self):
        return 
    
    def getInitialKeyListeners(self):
        return []
    
    def getInitialAccelerators(self):
        return []
