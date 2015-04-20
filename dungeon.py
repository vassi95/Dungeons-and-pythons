from hero import Hero
from exceptions import DungeonInvalid


class Dungeon:

    def __init__(self, filename):
        self._map_data = {
            "H": (-1, -1),
            "S": [],
            "T": [],
            "E": [],
            "#": [],
            ".": [],
            "size": (0, 0)
        }

        self._generate_map(filename)

    def spawn(self, hero):
        if not isinstance(hero, Hero):
            raise TypeError("No hero provided")

        if not len(self._map_data["S"]):
            return False

        spawn_point = self._map_data["S"][0]
        self._map_data["S"].remove(spawn_point)
        self._map_data["H"] = spawn_point

    def move_hero(self, direction):
        direction = (direction in ["up", "down"], direction in ["left", "right"])


    def print_map(self):
        map_size = self._map_data["size"]
        level = [["."] * map_size[1] for i in range(0, map_size[0])]

        for key in list(filter(lambda x: x != "size", self._map_data.keys())):
            if key == "H":
                if self._map_data[key] != (-1, -1):
                    level[self._map_data[key][0]][self._map_data[key][1]] = key
                continue

            for square in self._map_data[key]:
                level[square[0]][square[1]] = key

        [print("".join(row)) for row in level]

    def _generate_map(self, filename):
        with open(filename, "r") as f:
            level = [row for row in f.read().split("\n") if row.strip()]
            if not len(level):
                raise DungeonInvalid("The provided level is not valid.")

            self._map_data["size"] = (len(level), len(level[0]))

            pos = [0, 0]
            for row in level:
                for square in row:
                    if square in self._map_data.keys():
                        self._map_data[square].append(tuple(pos))
                    pos[1] += 1
                pos = [pos[0] + 1, 0]


if __name__ == '__main__':
    map = Dungeon("level1.txt")
    map.print_map()

    hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
    map.spawn(hero)
    map.print_map()