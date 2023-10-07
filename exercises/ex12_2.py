import sys
import pygame


class CentreCharacter:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.image = pygame.image.load("images/fornite_chick.bmp")
        self.rect = self.image.get_rect()
        self.rect.center = self.screen.get_rect().center
        pygame.display.set_caption("Centred Character")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.image, self.rect)
            pygame.display.flip()


if __name__ == '__main__':
    cc = CentreCharacter()
    cc.run_game()