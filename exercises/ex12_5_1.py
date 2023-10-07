import pygame
import sys

from time import sleep
from ex12_5_2 import Settings
from ex12_5_3 import Ship
from ex12_5_4 import Bullet
from ex12_5_5 import Alien
from ex12_5_6 import GameStats


class SidewaysAlienInvasion:
    """Overall class to manage the game"""
    def __init__(self):
        """Initializes the game's settings and variables"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width
        pygame.display.set_caption("Sideways Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stats = GameStats(self)

        self._create_fleet()

    def run_game(self):
        """Starts the main loop for the game"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        """Checks keyboard presses"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Processes key presses"""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Processes key releases"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Creates a new bullet and adds it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Updates all bullets positions and gets rid of the old ones"""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Checks and responds to bullet-alien collisions"""
        previous_size = len(self.aliens)
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        self.stats.aliens_hit += previous_size - len(self.aliens)
        if self.stats.aliens_hit >= self.settings.winning_alien_hits:
            print("You won!")
            self.stats.game_active = False
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """Updates alien's position and checks for collisions or aliens that have reached the end"""
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_left()

    def _ship_hit(self):
        """Responds to the ship getting hit"""
        self.stats.ships_left -= 1
        if self.stats.ships_left > 0:
            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            print("You lost!")
            self.stats.game_active = False

    def _check_aliens_left(self):
        """Check if aliens have reached the left"""
        for alien in self.aliens:
            if alien.rect.left < self.screen.get_rect().left:
                self._ship_hit()
                break

    def _create_fleet(self):
        """Creates a fleet of randomly placed aliens"""
        alien = Alien(self)
        alien_height = alien.rect.height
        number_aliens_y = self.settings.screen_height // (2 * alien_height)
        for i in range(number_aliens_y):
            self._create_alien()

    def _create_alien(self):
        """Creates a single alien and checks if it doesn't overlap with other aliens"""
        alien = Alien(self)
        while pygame.sprite.spritecollideany(alien, self.aliens):
            alien = Alien(self)
        self.aliens.add(alien)

    def _update_screen(self):
        """Processes the next frame of the screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    game = SidewaysAlienInvasion()
    game.run_game()
