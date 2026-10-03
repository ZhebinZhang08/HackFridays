import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My First Pygame CE Game")

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((40, 40, 40))

    pygame.draw.rect(screen, (0, 255, 128), (350, 250, 100, 100))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()