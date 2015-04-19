from weapon_spell import Weapon, Spell
import unittest


class weapon_test(unittest.TestCase):
    def setUp(self):
        self.weapon = Weapon("Weapon", 30)

    def test_init(self):
        self.assertEqual(self.weapon.name, "Weapon")
        self.assertEqual(self.weapon.damage, 30)


class spell_test(unittest.TestCase):
    def setUp(self):
        self.spell = Spell("Spell", 100, 30, 2)

    def test_init(self):
        self.assertEqual(self.spell.name, "Spell")
        self.assertEqual(self.spell.damage, 100)
        self.assertEqual(self.spell.mana_cost, 30)
        self.assertEqual(self.spell.cast_range, 2)

if __name__ == '__main__':
    unittest.main()
