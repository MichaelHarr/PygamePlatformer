import pygame
from data.window import Window
from data.userInput import UserInput
from data.world import World
from data.renderer import Renderer
from data.maploader import Maploader

class Game:

    def __init__(self):
        self.window = Window()
        self.UserInput = UserInput(self)
        self.world = World(self)
        self.renderer = Renderer(self)


    def update(self):
        self.UserInput.update()
        self.world.update()
        self.renderer.update()
        
    # Game Loop
    def run(self):  
        while True:
            self.update()


game = Game()
game.run()