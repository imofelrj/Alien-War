#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

import sys              # for exit
import pygame

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

def update_screen(ai_var,screen,ship):
    screen.fill(ai_var.bg_color)
    ship.blit_me()
    pygame.display.flip()