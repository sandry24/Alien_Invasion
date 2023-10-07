import json


class GameStats:
    """Track game statistics for Alien Invasion"""
    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        # Start Alien invasion in an active state
        self.game_active = False
        self.first_game = True

        # High score should never be reset
        self.high_score = self.get_stored_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def get_stored_high_score(self):
        """Get stored high score if available"""
        try:
            with open("high_score.json") as f:
                high_score = json.load(f)
        except FileNotFoundError:
            with open("high_score.json", "w") as f:
                json.dump(0, f)
            return 0
        else:
            return high_score
