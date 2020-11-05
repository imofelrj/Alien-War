#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

from bullet import Bullet
from alien import Alien
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

def check_events_key_down(ship,event,ai_var,screen,bullets):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:  # move right
            ship.moving_right = True
        elif event.key == pygame.K_q:    # exit
            pygame.quit()
            sys.exit(0)
        elif event.key == pygame.K_LEFT: # move left
            ship.moving_left = True
        elif event.key == pygame.K_UP:   # move up
            ship.moving_up = True
        elif event.key == pygame.K_DOWN: # move down
            ship.moving_down = True
        elif event.key == pygame.K_SPACE and len(bullets) < ai_var.bullet_maximum: # fire
            new_bullet = Bullet(ai_var,screen,ship)
            bullets.add(new_bullet)

def check_events(ship,ai_var,screen,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        check_events_key_down(ship,event,ai_var,screen,bullets)
        check_events_key_up(ship,event)

def update_screen(ai_var,screen,ship,bullets,aliens):
    screen.fill(ai_var.bg_color)
    for bullet in bullets.sprites():
        bullet.draw()
    ship.blit_me()
    for alien in aliens.sprites():
        alien.draw()
    pygame.display.flip()

def remove(bullets,aliens,screen):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen.get_rect().bottom:
            aliens.remove(alien)

def update_aliens(aliens,screen,ai_var,bullets):
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if len(aliens) == 0:
        for i in range(0,ai_var.alien_maximum):
            new_alien = Alien(screen,ai_var)
            aliens.add(new_alien)