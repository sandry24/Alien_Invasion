import sys
import pygame


class EmptyScreen:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Empty Screen")

    def run_game(self):
        while True:
            self._check_events()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key == pygame.K_q:
                    sys.exit()


if __name__ == "__main__":
    game = EmptyScreen()
    game.run_game()
    