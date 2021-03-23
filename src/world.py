import pygame
from src.player import Player
from src.block import Block
from src.maploader import Maploader

class World:

    def __init__(self, game):
        self.game = game
        self.player = Player(self)
        self.screen = self.game.window.get_screen()
        self.background_color = [70, 30, 150]
        self.level = 1
        self.maploader = Maploader(self)
        self.blocks = pygame.sprite.Group()
        self.someBlock = Block(50, 50, self)


    def get_window_size(self):
        return self.game.window.get_window_size()

    def get_screen(self):
        return self.game.window.get_screen()

    def next_level(self):
        self.level += 1

    def update(self):
        self.screen.fill(self.background_color)
        self.player.update()
        self.someBlock.update(self.someBlock.block_image, self.someBlock.get_pos())
        #for block in self.blocks:
        #    block.update()

