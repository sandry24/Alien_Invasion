import pygame
import sys

from ex13_3_2 import Droplet

class Rain:
    """Class to manage the assets of Rain program"""
    def __init__(self):
        """Initializes the game's assets and variables"""
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        self.bg_img = pygame.image.load("images/rainy_sky.jpg")
        self.bg_img = pygame.transform.scale(self.bg_img, (self.screen_width, self.screen_height))
        pygame.display.set_caption("Rain")

        self.droplets = pygame.sprite.Group()

        self._create_rain_row()

    def run_game(self):
        """Stars the main loop for running the game"""
        while True:
            self._check_events()
            self._update_droplets()
            self._update_screen()

    def _check_events(self):
        """Responds to key presses"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def _create_rain_row(self):
        """Creates a row of randomly offset droplets"""
        droplet = Droplet(self)
        droplet_width = droplet.droplet_width
        number_droplets_x = self.screen_width // (2 * droplet_width)
        for i in range(number_droplets_x * 3):
            self._create_droplet()

    def _create_droplet(self):
        """Creates a single droplet"""
        droplet = Droplet(self)
        self.droplets.add(droplet)

    def _update_droplets(self):
        """Updates the droplets' positions and gets rid of old ones"""
        self.droplets.update()

        for droplet in self.droplets.copy():
            if droplet.rect.top >= self.screen_height:
                self.droplets.remove(droplet)
                new_droplet = Droplet(self)
                self.droplets.add(new_droplet)

    def _update_screen(self):
        """Updates images and flip it to the new screen"""
        self.screen.blit(self.bg_img, (0, 0))
        for droplet in self.droplets.sprites():
            droplet.draw_droplet()
        pygame.display.flip()


if __name__ == "__main__":
    game = Rain()
    game.run_game()
