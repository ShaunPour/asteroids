import pygame
from constants import *
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock=pygame.time.Clock()
    clock
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill('Black')
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()