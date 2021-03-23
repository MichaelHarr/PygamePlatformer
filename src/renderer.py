import pygame

class renderer:

    def __init__(self, game):
        self.game = game
        self.clock = pygame.time.Clock()

    def update(self):
        pygame.display.update()
        self.clock.tick()