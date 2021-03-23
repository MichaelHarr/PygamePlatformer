class Entity:

    def __init__(self, x, y, world):
        self.x = x
        self.y = y
        self.world = world
        self.screen = self.world.get_screen()

    def get_pos(self):
        return [self.x, self.y]

    def update(self, image, location):
        self.screen.blit(image, location)

'''
    def update(self, image, location):
        self.screen.blit(image, location)
'''