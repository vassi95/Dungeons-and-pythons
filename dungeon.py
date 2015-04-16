
class Dungeon:

    def __init__(self, filename):
        self.filename = filename

    def print_map(self):
            with open("level1.txt", "r") as f:
                level1 = f.read().split("\n")
                print(level1)

map = Dungeon("level1.txt")
print(map.print_map())
