import pygame
from pygame.sprite import Sprite


class Life(Sprite):
    """A class to manage a single heart"""
    def __init__(self, ai_game):
        """Initializes the heart's assets"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load("images/minecraft_heart_transparent_icon.png")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
