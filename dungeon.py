from hero import Hero
from exceptions import DungeonInvalid


class Dungeon:

    def __init__(self, filename):
        self._map_data = {
            "S": [],
            "T": [],
            "E": [],
            "#": [],
            ".": [],
            "G": [],
            "H": (-1, -1),
            "size": (0, 0)
        }

        self._generate_map(filename)

    def spawn(self, hero):
        if not len(self._map_data["S"]):
            return False

        spawn_point = self._map_data["S"][0]
        self._map_data["S"].remove(spawn_point)
        self._map_data["H"] = spawn_point

    def print_map(self):
        map_size = self._map_data["size"]
        level = [["."] * map_size[1] for i in range(0, map_size[0])]

        for key in list(filter(lambda x: x != "size", self._map_data.keys())):
            if key == "H":
                if -1 not in self._map_data[key]:
                    level[self._map_data[key][0]][self._map_data[key][1]] = key
                continue

            for square in self._map_data[key]:
                if square != self._map_data["H"]:
                    level[square[0]][square[1]] = key

        for row in level:
            print("".join(row))

    def move_hero(self, direction):
        offset = -1 if direction in ["up", "left"] else 1
        multiplier = direction in ["up", "down"]  # 0 if left/right, 1 if up/down

        new_hero_pos = tuple(map(sum, zip(self._map_data["H"], (multiplier * offset, (not multiplier) * offset))))
        if (-1 in new_hero_pos or new_hero_pos in self._map_data["#"]
                or True in [self._map_data["size"][i] <= new_hero_pos[i] for i in range(0, 2)]):
            return False

        return self._trigger_square(new_hero_pos)

    def _trigger_square(self, hero_pos):
        if hero_pos in self._map_data["T"]:
            print("Found treasure.")
            # Do something when a treasure has been found
        elif hero_pos in self._map_data["E"]:
            print("Enemy!")
            # Fight the enemy

        self._map_data["H"] = hero_pos

        return True

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
    level = Dungeon("level1.txt")
    level.print_map()

    hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
    level.spawn(hero)
    level.print_map()

    path = ["up", "right", "down", "left", "down", "down", "right"]
    for direction in path:
        can_move = level.move_hero(direction)
        print("\nCan move %s?:" % direction, "yes" if can_move else "no")

        if can_move:
            level.print_map()
