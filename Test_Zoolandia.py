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

if __name__ == '__main__':
    unittest.main()
