import unittest
from hero import Hero
from weapon import Weapon
from spell import Spell
from exceptions import HeroAlreadyHasAWeapon


class TestHero(unittest.TestCase):

    def setUp(self):
        self._hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        self.super_hero = Hero(name="Bron", title="Dragonslayer", health=150, mana=150, mana_regeneration_rate=2)

    def test_init(self):
        self.assertTrue(isinstance(self._hero, Hero))

        with self.assertRaises(ValueError):
            Hero(name="Bron", title="Dragonslayer", health=-1, mana=100, mana_regeneration_rate=2)

        with self.assertRaises(ValueError):
            Hero(name="Bron", title="Dragonslayer", health=150, mana=100, mana_regeneration_rate=2)

        with self.assertRaises(ValueError):
            Hero(name="Bron", title="Dragonslayer", health=100, mana=-1, mana_regeneration_rate=2)

        with self.assertRaises(ValueError):
            Hero(name="Bron", title="Dragonslayer", health=100, mana=150, mana_regeneration_rate=2)

        with self.assertRaises(ValueError):
            Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=-1)

        with self.assertRaises(TypeError):
            Hero(name=0, title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

        with self.assertRaises(TypeError):
            Hero(name="Bron", title=0, health=100, mana=100, mana_regeneration_rate=2)

        with self.assertRaises(TypeError):
            Hero(name="Bron", title="Dragonslayer", health="str", mana=100, mana_regeneration_rate=2)

        with self.assertRaises(TypeError):
            Hero(name="Bron", title="Dragonslayer", health=100, mana="str", mana_regeneration_rate=2)

        with self.assertRaises(TypeError):
            Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate="str")

    def test_known_as(self):
        self.assertEqual(self._hero.known_as(), "Bron the Dragonslayer")

    def test_get_health(self):
        self.assertEqual(self._hero.get_health, self._hero.health)

        with self.assertRaises(ValueError):
            self.super_hero.get_health()

    def test_get_mana(self):
        self.assertEqual(self._hero.get_mana, self._hero.mana)

        with self.assertRaises(ValueError):
            self.super_hero.get_mana()

    def test_is_alive(self):
        self.assertTrue(self._hero.is_alive())

    def test_can_cast(self):
        self.assertTrue(self._hero.can_cast())

    def test_take_damage(self):
        self._hero.take_damage(30)
        self.assertEqual(self._hero.health, 70)

        with self.assertRaises(ValueError):
            self._hero.take_damage(-30)

    def test_take_healing(self):
        dead_hero = Hero(name="Bron", title="Dragonslayer", health=0, mana=100, mana_regeneration_rate=2)

        self.assertFalse(dead_hero.take_healing(30))

        with self.assertRaises(ValueError):
            self._hero.take_healing(30)

        damaged_hero = Hero(name="Bron", title="Dragonslayer", health=50, mana=100, mana_regeneration_rate=2)

        self.assertTrue(damaged_hero.take_healing(30))

    def test_take_mana(self):
        down_mana_hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=10, mana_regeneration_rate=2)
        down_mana_hero.take_mana(30)

        self.assertEqual(down_mana_hero.mana, 40)

        with self.assertRaises(ValueError):
            down_mana_hero.take_mana(-30)

    def test_equip(self):
        w1 = Weapon(name="The Axe of Destiny", damage=20)
        w2 = Weapon(name="Crescent Scimitar", damage=132)

        self._hero.equip(w2)

        with self.assertRaises(HeroAlreadyHasAWeapon):
            self._hero.equip(w1)

    def test_learn(self):
        s1 = Spell(name="Fireball", damage=30, mana_cost=20, cast_range=2)
        s2 = Spell(name="Earth Pulse", damage=50, mana_cost=20, cast_range=2)

        self._hero.learn(s1)

        self.assertEqual(self._hero.mana, 80)

        self._hero.learn(s2)

        self.assertEqual(self._hero.spell, s2)

    def test_attack(self):
        weapon = Weapon(name="Crescent Scimitar", damage=20)
        self.assertEqual(self._hero.attack(by=weapon), 0)

        self._hero.equip(weapon)

        self.assertEqual(self._hero.attack(by=weapon), weapon.damage)
