import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class to manage the bullets fired by the ship"""
    def __init__(self, game):
        """Initializes the bullet's properties"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = game.ship.rect.midright

        self.x = float(self.rect.x)

    def update(self):
        """Updates the bullet's position"""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        """Draws the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
