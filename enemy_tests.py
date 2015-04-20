import unittest
from enemy import Enemy


class TestEnemy(unittest.TestCase):

    def setUp(self):
        self._enemy = Enemy(health=100, mana=100, damage=20)

    def test_init(self):
        self.assertTrue(isinstance(self._enemy, Enemy))

        with self.assertRaises(ValueError):
            Enemy(health=-1, mana=100, damage=20)

        with self.assertRaises(ValueError):
            Enemy(health=150, mana=100, damage=20)

        with self.assertRaises(ValueError):
            Enemy(health=100, mana=-1, damage=20)

        with self.assertRaises(ValueError):
            Enemy(health=100, mana=150, damage=20)

        with self.assertRaises(ValueError):
            Enemy(health=100, mana=100, damage=-20)

        with self.assertRaises(TypeError):
            Enemy(health="str", mana=100, damage=20)

        with self.assertRaises(TypeError):
            Enemy(health=100, mana="str", damage=20)

        with self.assertRaises(TypeError):
            Enemy(health=100, mana=100, damage="str")

    def test_get_health(self):
        self.assertEqual(self._enemy.get_health(), self._enemy.health)

    def test_get_mana(self):
        self.assertEqual(self._enemy.get_mana(), self._enemy.mana)

    def test_is_alive(self):
        self.assertTrue(self._enemy.is_alive())

    def test_can_cast(self):
        self.assertTrue(self._enemy.can_cast())

    def test_take_healing(self):
        damaged_enemy = Enemy(health=50, mana=100, damage=20)

        self.assertTrue(damaged_enemy.take_healing(30))

    def test_take_mana(self):
        down_mana_enemy = Enemy(health=100, mana=40, damage=20)
        down_mana_enemy.take_mana(30)
        self.assertEqual(down_mana_enemy.mana, 40)

    def test_attack(self):
        pass

if __name__ == '__main__':
    unittest.main()
