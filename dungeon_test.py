import unittest
from dungeon import Dungeon
from hero import Hero


class TestEnemy(unittest.TestCase):

    def setUp(self):
        self._hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        self.filename = Dungeon(filename="level1.txt")

    def test_init(self):
        self.assertTrue(isinstance(self.filename, Dungeon))
        with self.assertRaises(TypeError):
            Dungeon(filename=int)

    def test_spawn(self):
        pass


if __name__ == '__main__':
    unittest.main()
