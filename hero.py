
class Hero():
    def __init__(self, title, health, mana, mana_regeneration_rate):
        self.title = title
        self.health = health
        self.c_health = health
        self.mana = mana
        self.weapon = False
        self.m_mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def is_alive(self):
        if self.get_c_health() > 0:
            return True
        return False

    def get_health(self):
        return self.c_health

    def get_mana(self):
        return self.mana

    def can_cast(self):
        if self.get_mana() > 0:
            return True
        return False

    def take_damage(self, damage_points):
        if damage_points > self.c_health:
            self.c_health = 0
        else:
            self.c_health -= damage_points
        return self.c_health

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False

        self.health += healing_points
        if self.health > self.c_health:
            self.health = self.c_health
        return True

    def take_mana(self, mana_points):
        new = 0
        if self.move_hero():
            new += self.mana_regeneration_rate
        new += mana_points
        self.mana += new
        if self.mana > self.m_mana:
            self.mana = self.m_mana

    def has_weapon(self):
        return self.weapon is not False

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def learn_spell(self, spell):
        self.spell = spell

    def attack(self, by):
        if not self.has_weapon() or not self.learn_spell():
            return 0
        if by != "magic" or by != "weapon":
            return False
        if by == "weapon":
            return self.weapon.damage
        if by == "magic" and self.can_cast():
            return self.magic.damage
