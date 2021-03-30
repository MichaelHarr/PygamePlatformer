import pygame
from entity import Entity

class Player(Entity):
    
    def __init__(self, world):
        super().__init__(50, 50, world)
        self.player_image = pygame.image.load("Square.png")
        self.player_location = [self.x, self.y]
        self.player_v_momentum = 0
        self.screen = self.world.get_screen()
        self.is_moving_right = False
        self.is_moving_left = False
        self.speed = 5


    
    def update(self): 

        self.screen.blit(self.player_image, self.player_location)

        # Makes player bounce when they reach bottom of window
        if self.player_location[1] >= self.world.get_window_size()[0] - 550:
            self.player_v_momentum = -(self.player_v_momentum)
        else:
            self.player_v_momentum += 0.03
        self.player_location[1] += self.player_v_momentum

        if self.is_moving_right == True:
            self.player_location[0] += self.speed
        if self.is_moving_left == True:
            self.player_location[0] -= self.speed
