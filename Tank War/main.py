#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

import sys                                # for exit
import pygame                             # pygame
from var import Var                       # for const

def main():
    pygame.init()
    ai_var = Var();
    screen = pygame.display.set_mode(
        [ai_var.screen_width,ai_var.screen_height])
    pygame.display.set_caption("Tank War")

    while True:                           # Game Started
        for event in pygame.event.get():  # Listening on keys
            if event.type == pygame.QUIT:
                sys.exit(0)               # QUIT
        screen.fill(ai_var.bg_color)
        pygame.display.flip()

main()