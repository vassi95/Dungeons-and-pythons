

class Weapon:

    def __init__(self, name, damage):
        self._name = name
        self._damage = damage


class Spell:

    def __init__(self, name, damage, mana_cost, cast_range):
        self._name = name
        self._damage = damage
        self._mana_cost = mana_cost
        self._cast_range = cast_range
