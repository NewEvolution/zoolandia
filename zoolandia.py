class Animal:
    def __init__(self):
        self.species = ''
        self.name = ''

class Species:
    def __init__(self):
        self.common_name = ''
        self.geo_region = ''

class Habitat:
    def __init__(self):
        self.name = ''
        self.members = set()

class Walking:
    def __init__(self):
        self.walk_speed = 0
        self.legs = 0
