import pygame.font
from random import randint


class RandomBuff:
    """A class to manage in-game buffs"""
    def __init__(self, ai_game):
        """Initializes assets"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (30, 30, 30)
        self.index = 0
        self.font = pygame.font.SysFont(None, 48)
        self.powerups = ["", "+1 Life", "+5000 Score", "+10000 Score", "2x Score Multiplier", "+ Speed"]

        self._prep_powerup()

    def _choose_powerup(self):
        """Chooses a random powerup"""
        random = randint(1, 100)
        if random <= 10:
            self.stats.ships_left += 1
            self.font_color = (255, 0, 0)
            self.index = 1
        elif random <= 50:
            self.stats.score += 5000
            self.font_color = (0, 0, 0)
            self.index = 2
        elif random <= 80:
            self.stats.score += 10000
            self.font_color = (0, 0, 0)
            self.index = 3
        elif random <= 90:
            self.settings.alien_points *= 2
            self.font_color = (255, 255, 0)
            self.index = 4
        elif random <= 100:
            self.settings.ship_speed *= self.settings.speedup_scale
            self.settings.bullet_speed *= self.settings.speedup_scale
            self.font_color = (0, 255, 255)
            self.index = 5
        self.ai_game.sb.prep_score()
        self.ai_game.sb.check_high_score()
        self.ai_game.sb.prep_ships()
        self._prep_powerup()

    def _prep_powerup(self):
        """Turn the buff into a rendered image"""
        str_buff = self.powerups[self.index]
        self.powerup_img = self.font.render(str_buff, True, self.text_color, None)

        self.powerup_rect = self.powerup_img.get_rect()
        self.powerup_rect.x = 10
        self.powerup_rect.y = 70

    def show_powerup(self):
        """Displays powerup to screen"""
        self.screen.blit(self.powerup_img, self.powerup_rect)
