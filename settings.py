import pygame


class Settings:
    """A class to store all settings for Alien Invasion"""
    def __init__(self):
        """Initializes the game's static settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.play_menu = pygame.image.load("images/alien_invasion_menu.png")
        self.game_over_menu = pygame.image.load("images/game_over_screen.png")
        # self.bg_img = pygame.image.load("images/stars_background.jpg")

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (225, 193, 110)
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10

        # Mystery Drop settings
        self.mystery_drop_speed = 1.0

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.mystery_drop_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
