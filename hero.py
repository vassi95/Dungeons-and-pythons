from exceptions import HeroAlreadyHasAWeapon


class Hero():

    def __init__(self, name="Bron", title="Dragonslayer", health="100", mana="100", mana_regeneration_rate=2):

        if not isinstance(name, str):
            raise TypeError("Hero name not valid!")

        if not isinstance(title, str):
            raise TypeError("Hero title not valid!")

        if not isinstance(health, int):
            raise TypeError("Hero health not valid!")

        if not isinstance(mana, int):
            raise TypeError("Hero mana not valid!")

        if not isinstance(mana_regeneration_rate, int):
            raise TypeError("Hero mana_regeneration_rate not valid!")

        if health <= 0:
            raise ValueError("Hero has no health!")

        if mana < 0:
            raise ValueError("Mana value not appropriate!")

        if mana_regeneration_rate <= 0:
            raise ValueError("Mana_regeneration_rate value not appropriate!")

        if health > 100:
            raise ValueError("Too much health, not a super hero!")

        if mana > 100:
            raise ValueError("Too much mana for our hero!")
        self._name = name
        self._spell = False
        self._title = title
        self._health = health
        self._mana = mana
        self._weapon = False
        self._m_mana = mana
        self._mana_regeneration_rate = mana_regeneration_rate

    def known_as(self):
        return "{} the {}".format(self._name, self._title)

    def is_alive(self):
        if self._health > 0:
            return True
        return False

    def get_health(self):
        return self._health

    def get_mana(self):
        return self._mana

    def can_cast(self):
        if self.get_mana() > 0:
            return True
        return False

    def take_damage(self, damage_points):
        if damage_points <= 0:
            raise ValueError("Inappropriate damage_points argument value!")

        if damage_points > self._health:
            self._health = 0
        else:
            self._health -= damage_points

    def take_healing(self, healing_points):
        if healing_points <= 0:
            raise ValueError("Inappropriate healing_points argument value!")
        if not self.is_alive():
            return False

        if self._health + healing_points > 100:
            self._health = 100
        else:
            self._health += healing_points
        return True

    def take_mana(self, mana_points):
        new = 0
        if self.move_hero():
            new += self._mana_regeneration_rate
        new += mana_points
        self._mana += new
        if self._mana > self.m_mana:
            self._mana = self.m_mana

    def equip(self, weapon):
        if self._weapon:
            raise HeroAlreadyHasAWeapon("Our hero already has a weapon!")
        self._weapon = weapon

    def learn(self, spell):
        self._spell = spell

    def attack(self, by):
        if not self._weapon and not self._spell:
            return 0
        if by == "weapon":
            return self._weapon.damage
        if by == "magic" and self.can_cast():
            return self._mana.damage
