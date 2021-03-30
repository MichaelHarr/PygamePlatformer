import pygame
from entity import Entity

class Block(Entity):

    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.block_image = pygame.image.load("Square.png")
'''
    
    def update(self): 
        
        self.screen.blit(self.block_image, self.get_pos())


'''