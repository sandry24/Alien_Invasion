import pygame
from pygame.sprite import Sprite


class MysteryDrop(Sprite):
    """A class to manage a mystery drop from aliens"""
    def __init__(self, ai_game):
        """Initializes the drop's assets"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load("images/mystery_drop.png")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

    def update(self):
        """Move the drop downwards"""
        self.y += self.settings.mystery_drop_speed
        self.rect.y = self.y
