class Settings:
    """Class to manage the settings for the game"""
    def __init__(self):
        """Initializes the game's settings"""
        # Screen settings
        self.screen_height = 720
        self.screen_width = 1080
        self.bg_color = (230, 230, 230)

        self.ship_speed = 1.5
        self.ship_limit = 3

        self.bullet_speed = 2.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (225, 193, 110)
        self.bullets_allowed = 1000

        self.alien_speed = 0.5
        self.winning_alien_hits = 45
