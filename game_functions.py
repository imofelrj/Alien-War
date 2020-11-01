#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

from ship import Ship
import sys              # for exit
import pygame

def check_events_key_up(ship,event):
    if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
            elif event.key == pygame.K_UP:
                ship.moving_up = False
            elif event.key == pygame.K_DOWN:
                ship.moving_down = False

def check_events_key_down(ship,event):
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
            elif event.key == pygame.K_UP:
                ship.moving_up = True
            elif event.key == pygame.K_DOWN:
                ship.moving_down = True
def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        check_events_key_down(ship,event)
        check_events_key_up(ship,event)
def update_screen(ai_var,screen,ship):
    screen.fill(ai_var.bg_color)
    ship.blit_me()
    pygame.display.flip()