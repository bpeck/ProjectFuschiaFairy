from Arena import Arena
from CircleGuy import CircleGuy

class TestArena(Arena):
    
    def __init__(self):
        c = CircleGuy()
    
        self.entities = [c]
        self.keyListeners = [c]
    
    def getInitialEntities(self):
        return self.entities
    
    def getInitialKeyListeners(self):
        return self.keyListeners
