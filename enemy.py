
class Enemy:
    def __init__(self, health=100, mana=100, damage=20):
        self.health = health
        self.m_health = health
        self.m_mana = mana
        self.mana = mana
        self.damage = damage
        if health <= 0:
            raise ValueError("Hero has no health!")

        if health > 100:
            raise ValueError("Too much health, not a super hero!")
        if mana < 0:
            raise ValueError("Mana value not appropriate!")
        if mana > 100:
            raise ValueError("Too much mana for our hero!")
        if damage <= 0:
            raise ValueError("Damage value not appropriate")
        if not isinstance(health, int):
            raise TypeError("Hero health not valid!")

        if not isinstance(mana, int):
            raise TypeError("Hero mana not valid!")

        if not isinstance(damage, int):
            raise TypeError("damage not valid!")

    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def can_cast(self):
        if self.mana > 0:
            return True
        return False

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False

        self.health += healing_points
        if self.health > self.m_health:
            self.health = self.m_health
        return True

    def take_mana(self, mana_points):
        if mana_points + self.mana > self.m_mana:
            self.mana = self.m_mana
            return True
        else:
            self.mana += mana_points
            return True

    def attack(self, by):
        if not self.has_weapon() or not self.learn_spell():
            return 0
        if by != "magic" or by != "weapon":
            return False
        if by == "weapon":
            return self.weapon.damage
        if by == "magic" and self.can_cast():
            return self.magic.damage

