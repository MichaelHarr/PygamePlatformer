import pygame
from src.window import Window
from src.input import Input
from src.world import World
from src.renderer import renderer
from src.maploader import Maploader

class Game:

    def __init__(self):
        self.window = Window()
        self.input = Input(self)
        self.world = World(self)
        self.renderer = renderer(self)


    def update(self):
        self.input.update()
        self.world.update()
        self.renderer.update()
        
    # Game Loop
    def run(self):  
        while True:
            self.update()


game = Game()
game.run()