import pygame
from pygame.sprite import Sprite
from random import randint


class Alien(Sprite):
    """Class to represent a single alien"""
    def __init__(self, game):
        """Initializes the alien's assets"""
        super().__init__()
        self.screen = game.screen
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        self.settings = game.settings

        self.image = pygame.image.load("images/alien_side.bmp")
        self.rect = self.image.get_rect()
        self.rand_lb_x = self.screen_width // 2
        self.rand_ub_x = self.screen_width - self.rect.width
        self.rand_lb_y = 0
        self.rand_ub_y = self.screen_height - self.rect.height

        self.rect.x = randint(self.rand_lb_x, self.rand_ub_x)
        self.rect.y = randint(self.rand_lb_y, self.rand_ub_y)

        self.x = float(self.rect.x)

    def update(self):
        """Updates the alien's position"""
        self.x -= self.settings.alien_speed
        self.rect.x = self.x
