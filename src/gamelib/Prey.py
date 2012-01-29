from NPC import NPC

class Prey(NPC):
    
    def __init__(self, size, position, maxRotVel, maxRotAcc):
        NPC.__init__(self, size, position, maxRotVel, maxRotAcc)
        self.name = 'Prey'
        self.lifeSpan = 10000
    
    def update(self, dT):
        NPC.update(self, dT)
        self.lifeSpan -= dT
        if self.lifeSpan < 0:
            self.lifeSpan = 10000
