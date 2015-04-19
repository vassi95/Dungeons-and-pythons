from weapon_spell import Weapon, Spell
import unittest


class weapon_test(unittest.TestCase):
    def setUp(self):
        self.weapon = Weapon("Weapon", 20)

    def test_init(self):
        self.assertEqual(self.weapon.name, "Weapon")
        self.assertEqual(self.weapon.damage, 20)


class spell_test(unittest.TestCase):
    def setUp(self):
        self.spell = Spell("Spell", 100, 20, 3)

    def test_init(self):
        self.assertEqual(self.spell.name, "Spell")
        self.assertEqual(self.spell.damage, 100)
        self.assertEqual(self.spell.mana_cost, 20)
        self.assertEqual(self.spell.cast_range, 3)

if __name__ == '__main__':
    unittest.main()
