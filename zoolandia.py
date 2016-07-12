class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Species:
    def __init__(self):
        self.common_name = ''
        self.geo_region = ''

class BettaTrifasciata(Species):
    def __init__(self, color):
        self.color = color
        self.common_name = 'Betta'

class Betta(Animal):
    def __init__(self, color, name):
        Animal.__init__(self, name, BettaTrifasciata(color))

class Habitat:
    def __init__(self):
        self.name = ''
        self.members = set()

    def add_member(self, member):
        self.members.add(member)

class Aquarium(Habitat):
    def __init__(self, water_type):
        self.water_type = water_type

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
        self.swim_speed = 0
        self.fins = False
        self.flippers = False
        self.web_feet = False
