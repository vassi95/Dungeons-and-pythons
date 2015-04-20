import unittest
from dungeon import Dungeon


class TestEnemy(unittest.TestCase):

    def setUp(self):
        self.filename = Dungeon(filename="level1.txt")

    def test_init(self):
        self.assertTrue(isinstance(self.filename, Dungeon))
        with self.assertRaises(TypeError):
            Dungeon(filename=int)

    def test_spawn(self):
        pass


if __name__ == '__main__':
    unittest.main()
