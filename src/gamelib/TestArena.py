from Arena import Arena
from CircleGuy import CircleGuy
from MouseEntity import MouseEntity

class TestArena(Arena):
    
    def __init__(self):
        c = CircleGuy()
        
        m = MouseEntity()
    
        self.entities = [c, m]
        self.keyListeners = [c, m]
    
    def getInitialEntities(self):
        return self.entities
    
    def getInitialKeyListeners(self):
        return self.keyListeners
