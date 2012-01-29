""" Arena class is in charge of initializing a play-space, and supplying our
Game class with a list of entities to render and update """

class Arena(object):
    
    def __init__(self):
        self.entities = []
        self.keyListeners = []
    
    def findCollisions(self):
        collisions = []
        for i in self.entities:
            if not i.collides: continue
            for j in self.entities:
                if not j.collides or i==j: continue
                if i.pos.distance_squared(j.pos) < (i.radius+j.radius)**2:
                    collisions.append((i, j))
        return collisions
    
    def getInitialEntities(self):
        return 
    
    def getInitialKeyListeners(self):
        return []
