import sys
import pygame

from ex13_1_2 import Star
from random import randint


class StarGrid:
    """General class to manage a grid of stars"""
    def __init__(self):
        """Initializes the game and game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        self.stars = pygame.sprite.Group()
        self.bg_img = pygame.image.load("images/sky.jpg")
        self.bg_img = pygame.transform.scale(self.bg_img, (self.screen_width, self.screen_height))
        pygame.display.set_caption("Star Grid")

        self._create_stars()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Responds to key presses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Responds to key presses"""
        if event.key == pygame.K_q:
            sys.exit()

    def _create_stars(self):

        """Creates a group of stars"""
        star = Star(self)
        star_width, star_height = star.rect.size
        current_x = star_width
        current_y = star_height

        while current_y <= self.screen_height - 2 * star_height:
            current_x = star_width
            while current_x <= self.screen_width - 2 * star_width:
                self._create_star(current_x, current_y)
                current_x += 2 * star_width
            current_y += 2 * star_height

    def _create_star(self, current_x, current_y):
        """Create a star and place it"""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x, star.y = self._random_offset_star(current_x, current_y, star_width, star_height)
        star.rect.x = star.x
        star.rect.y = star.y
        self.stars.add(star)

    def _random_offset_star(self, current_x, current_y, star_width, star_height):
        """Returns randomly offset position of the star"""
        limit_rand_x = star_width // 2
        limit_rand_y = star_height // 2
        rand_x = randint(-limit_rand_x, limit_rand_x)
        rand_y = randint(-limit_rand_y, limit_rand_y)
        while current_x + rand_x < 0 or current_x + star_width + rand_x > self.screen_width:
            rand_x = randint(-limit_rand_x, limit_rand_x)
        while current_y + rand_y < 0 or current_y + star_height + rand_y > self.screen_height:
            rand_y = randint(-limit_rand_y, limit_rand_y)
        return rand_x + current_x, rand_y + current_y

    def _update_screen(self):
        """Update images on the screen and flip to the new screen"""
        # self.screen.fill((25, 25, 112))
        self.screen.blit(self.bg_img, (0, 0))
        self.stars.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    # Make an instance and run the game
    game = StarGrid()
    game.run_game()