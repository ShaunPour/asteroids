import pygame
from constants import *
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill('Black')
        pygame.display.flip()

if __name__ == "__main__":
    main()