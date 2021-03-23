import pygame


class Window:

    def __init__(self):
        pygame.init()
        self.WINDOW_SIZE = (1300, 700)
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE, 0, 32)

    def get_window_size(self):
        return self.WINDOW_SIZE
        
    def get_screen(self):
        return self.screen