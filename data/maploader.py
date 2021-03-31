from .block import Block

class Maploader:

    def __init__(self, world):
        self.world = world

    
    def load(self, level_num):
        path = "src/Levels/level1.txt"
        with open(path) as f:
            map_txt = f.read()

        col = 0
        row = 0

        for line in map_txt.split("\n"):
            for char in line:
                if char == "0":
                    block = Block(col, row)
                    self.world.blocks.add(block)
            col += 25
        row += 25
                



