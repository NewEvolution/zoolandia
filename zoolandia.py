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

class Flying:
    def __init__(self):
        self.wings = 0
        self.wing_span = 0
        self.air_speed = 0

class Swimming:
    def __init__(self):
        self.fins = False
        self.flippers = False
        self.web_feet = False
