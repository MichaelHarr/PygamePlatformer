import pygame, sys
from pygame.locals import *


class UserInput:

    def __init__(self, game):
        self.game = game

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    self.game.world.player.is_moving_right = True
                    self.game.world.player.is_moving_left = False
                if event.key == K_LEFT:
                    self.game.world.player.is_moving_left = True
                    self.game.world.player.is_moving_right = False
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    self.game.world.player.is_moving_right = False
                if event.key == K_LEFT:
                    self.game.world.player.is_moving_left = False

