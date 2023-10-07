class GameStats:
    """A class that keeps track of the player's stats"""
    def __init__(self, game):
        """Initialize statistics"""
        self.settings = game.settings
        self.reset_stats()

        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
