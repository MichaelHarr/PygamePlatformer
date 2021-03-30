import pygame
from window import Window
from userInput import UserInput
from world import World
from renderer import renderer
from maploader import Maploader

class Game:

    def __init__(self):
        self.window = Window()
        self.UserInput = UserInput(self)
        self.world = World(self)
        self.renderer = renderer(self)


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