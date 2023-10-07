import sys
import pygame

from time import sleep
from ex14_2_2 import Ship
from ex14_2_3 import Settings
from ex14_2_4 import Box
from ex14_2_5 import Button
from ex14_2_6 import Bullet
from ex14_2_7 import GameStats


class TargetPractice:
    """Simple class to manage the target practice game"""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width
        pygame.display.set_caption("Target Practice")

        # Create an instance to store game statistics
        self.stats = GameStats(self)

        self.box = Box(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        # Make the play button
        self.play_button = Button(self, "Play")
        self.easy_button = Button(self, "Easy")
        self.easy_button.rect.x = self.settings.screen_width / 3 - self.easy_button.width/2
        self.easy_button.msg_image_rect.center = self.easy_button.rect.center
        self.hard_button = Button(self, "Hard")
        self.hard_button.rect.x = self.settings.screen_width / 3 * 2 - self.hard_button.width/2
        self.hard_button.msg_image_rect.center = self.hard_button.rect.center
        self.hard_mode = False

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_box()

            self._update_screen()

    def _check_events(self):
        """Responds to key presses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play"""
        #button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        #if button_clicked and not self.stats.game_active:
        #    self._start_game()
        button_clicked = self.easy_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._start_game()
        button_clicked = self.hard_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.hard_mode = True
            self._start_game()

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
        elif event.key == pygame.K_p:
            self._start_game()

    def _check_keyup_events(self, event):
        """Processes key releases"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _start_game(self):
        """Starts the game after interacting with the play button or a shortcut"""
        # Reset the game statistics
        self.stats.reset_stats()
        self.stats.game_active = True

        self.bullets.empty()

        # Create a new box and center the ship
        self.box.center_box()
        self.ship.center_ship()

        # Reset the game settings
        self.settings.initialize_dynamic_settings()
        for i in range(3):
            self.settings.increase_speed()
        self.hard_mode = False
        # Hide the mouse cursor
        pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        """Creates a new bullet and adds it to the bullets group"""
        if not self.stats.game_active:
            return
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Updates all bullets positions and gets rid of the old ones"""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)
                self._missed_hit()
                print(self.stats.ships_left)

        self._check_bullet_box_collisions()

    def _check_bullet_box_collisions(self):
        """Checks and responds to bullet-box collisions"""
        collisions = pygame.sprite.spritecollide(self.box, self.bullets, True)

    def _update_box(self):
        """Updates box position"""
        self.box.update()
        if self.box.time % 10000 == 0:
            self.settings.increase_speed()
        self._check_box_edges()

    def _check_box_edges(self):
        """Respond appropriately if the box has reached an edge"""
        if self.box.rect.y <= 0 or self.box.rect.bottom >= self.screen.get_height():
            self.settings.box_direction *= -1

    def _missed_hit(self):
        """Responds to the ship getting hit"""
        self.stats.ships_left -= 1
        if self.stats.ships_left == 0:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        """Processes the next frame of the screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.box.draw()
        if not self.stats.game_active:
            self.easy_button.draw_button()
            self.hard_button.draw_button()
        pygame.display.flip()


if __name__ == "__main__":
    game = TargetPractice()
    game.run_game()
