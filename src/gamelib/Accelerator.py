from CircleGuy import CircleGuy
from Entity import Entity
from Util import clamp

class Accelerator(Entity):
    
    def __init__(self, accFactor, minAcc, maxAcc):
        Entity.__init__(self)
        
        self.accFactor = accFactor
        self.minAcc = minAcc
        self.maxAcc = maxAcc
    
    def affectEntity(self, entity):
        if isinstance(entity, Accelerator):
            return
        if isinstance(entity, CircleGuy):
            return
    
        dist = self.pos.distance(entity.pos)
        
        accChange = 0.0
        if dist > 0.0:
            accChange = clamp((1.0/dist) * self.accFactor, self.minAcc, self.maxAcc)
        
        # make a vector pointing towards the accelerator
        towardsAcc = self.pos - entity.pos
        towardsAcc.normalize(1.0)
        
        # add some amount of accerlation to entity towards the accelerator
        # at a rate inverse to distance
        entity.acc += towardsAcc * accChange
