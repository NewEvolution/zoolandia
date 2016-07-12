class Animal:
    def __init__(self):
        self.species = None
        self.name = ''

class Species:
    def __init__(self):
        self.commonname = ''
        self.georegion = ''

class Habitat:
    def __init__(self):
        self.name = ''
        self.members = set()
