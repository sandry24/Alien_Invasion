import pygame


class Box:
    """A class to manage the target box"""
    def __init__(self, game):
        """Initializes the ship's settings and appearance"""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings

        self.color = (0, 0, 0)
        self.rect = pygame.Rect(0, 0, 400, 400)
        self.rect.midright = self.screen_rect.midright
        self.y = float(self.rect.y)
        self.time = 0

    def update(self):
        """Update the ship's location based on movement flags"""
        self.y += (self.settings.box_speed * self.settings.box_direction)
        self.rect.y = self.y
        self.time += 1

    def center_box(self):
        """Resets the box_position"""
        self.rect.midright = self.screen_rect.midright
        self.y = self.rect.y

    def draw(self):
        """Draw the box at its current location"""
        pygame.draw.rect(self.screen, self.color, self.rect)
