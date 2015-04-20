

class Treasure:
    def __init__(self, name):
        self._name = name
        self._increases_mana = False
        self._increases_health = False
        self._increase_value = 0
        self._found_weapon = False
        self._found_spell = False
        self._weapon_or_spell_name = " "
