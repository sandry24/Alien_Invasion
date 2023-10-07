import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """A class to represent a single star"""
    def __init__(self, game):
        """Initializes the star and sets its starting position"""
        super().__init__()
        self.screen = game.screen

        self.image = pygame.image.load("images/star.png")
        # self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
