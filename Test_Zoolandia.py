import unittest
import zoolandia

class TestAnimal(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    def test_name_emtpy_string_default(self):
        animal = zoolandia.Animal()
        self.assertEqual(animal.name, '')

    def test_species_emtpy_string_default(self):
        animal = zoolandia.Animal()
        self.assertEqual(animal.species, '')

class TestSpecies(unittest.TestCase):

    def test_commonname_emtpy_string_default(self):
        species = zoolandia.Species()
        self.assertEqual(species.common_name, '')

    def test_georegion_emtpy_string_default(self):
        species = zoolandia.Species()
        self.assertEqual(species.geo_region, '')

class TestHabitat(unittest.TestCase):

    def test_name_empty_string_default(self):
        habitat = zoolandia.Habitat()
        self.assertEqual(habitat.name, '')

    def test_members_set_default(self):
        habitat = zoolandia.Habitat()
        self.assertIsInstance(habitat.members, set)

class TestWalking(unittest.TestCase):

    def test_legs_zero_default(self):
        walking = zoolandia.Walking()
        self.assertEqual(walking.legs, 0)

    def test_walk_speed_zero_default(self):
        walking = zoolandia.Walking()
        self.assertEqual(walking.walk_speed, 0)

class TestSwimming(unittest.TestCase):

    def test_appendages_zero_default(self):
        swimming = zoolandia.Swimming()
        self.assertFalse(swimming.fins)
        self.assertFalse(swimming.flippers)
        self.assertFalse(swimming.web_feet)

    def test_swim_speed_zero_default(self):
        swimming = zoolandia.Swimming()
        self.assertEqual(swimming.swim_speed, 0)

class TestFlying(unittest.TestCase):

    def test_wings_zero_default(self):
        flying = zoolandia.Flying()
        self.assertEqual(flying.wings, 0)

    def test_wingspan_zero_default(self):
        flying = zoolandia.Flying()
        self.assertEqual(flying.wing_span, 0)

    def test_walk_speed_zero_default(self):
        flying = zoolandia.Flying()
        self.assertEqual(flying.air_speed, 0)

if __name__ == '__main__':
    unittest.main()
