import pygame
import sys

pygame.init()
GREEN = (0,255,0)
radius = 50
screen = pygame.display.set_mode([800,600])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
    pygame.draw.circle(screen,GREEN,(100,100),radius)
    pygame.display.update()
