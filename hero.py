
from weapon_spell import Weapon
from weapon_spell import Spell


class Hero():

    def __init__(self, name="Bron", title="Dragonslayer", health="100", mana="100", mana_regeneration_rate=2):
        self._name = name
        self._spell = False
        self._title = title
        self._health = health
        self._c_health = health
        self._mana = mana
        self._weapon = False
        self._m_mana = mana
        self._mana_regeneration_rate = mana_regeneration_rate

    def known_as(self):
        return "{} the {}".format(self._name, self._title)

    def is_alive(self):
        if self.get_c_health() > 0:
            return True
        return False

    def get_health(self):
        return self._c_health

    def get_mana(self):
        return self._mana

    def can_cast(self):
        if self.get_mana() > 0:
            return True
        return False

    def take_damage(self, damage_points):
        if damage_points > self._c_health:
            self._c_health = 0
        else:
            self._c_health -= damage_points
        return self._c_health

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False

        self._health += healing_points
        if self._health > self._c_health:
            self._health = self._c_health
        return True

    def take_mana(self, mana_points):
        new = 0
        if self.move_hero():
            new += self._mana_regeneration_rate
        new += mana_points
        self._mana += new
        if self._mana > self.m_mana:
            self._mana = self.m_mana

    def has_weapon(self):
        return self._weapon is not False

    def equip_weapon(self, weapon):
        self._weapon = weapon

    def learn_spell(self, spell):
        self._spell = spell

    def attack(self, by):
        if not self.has_weapon() or not self.learn_spell():
            return 0
        if by != "magic" or by != "weapon":
            return False
        if by == "weapon":
            return self.weapon.damage
        if by == "magic" and self.can_cast():
            return self.magic.damage
