""" Arena class is in charge of initializing a play-space, and supplying our
Game class with a list of entities to render and update """

class Arena(object):
    
    def __init__(self):
        self.entities = []
        self.keyListeners = []
    
    def getInitialEntities(self):
        return 
    
    def getInitialKeyListeners(self):
        return []
