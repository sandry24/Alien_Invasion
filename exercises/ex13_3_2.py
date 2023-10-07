import pygame
from pygame.sprite import Sprite
from random import randint


class Droplet(Sprite):
    """A class to manage a single rain droplet"""
    def __init__(self, game):
        """Initializes the droplet's assets"""
        super().__init__()
        self.screen = game.screen
        self.droplet_width = 5
        self.droplet_height = 10
        # self.color = (0, 60, 255)
        self.color = (255, 255, 255)
        self.drop_speed = randint(1, 3)

        self.rect = pygame.Rect(0, 0, self.droplet_width, self.droplet_height)
        self.rect.x = randint(0, self.screen.get_rect().width-self.droplet_width)
        self.rect.y = randint(-100*self.droplet_height, -self.droplet_height)

        self.y = float(self.rect.y)

    def update(self):
        """Moves the bullet down the screen"""
        self.y += self.drop_speed
        self.rect.y = self.y

    def draw_droplet(self):
        """Draws the droplet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

