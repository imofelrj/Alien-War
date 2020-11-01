#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

import pygame           # pygame
import sys
from pygame.sprite import Group
from pygame.sprite import Sprite

class Ship():
    def __init__(self,screen):
        self.screen = screen
        # load image and get its shape
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # make each new ship in the center of screen bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def blit_me(self):
        self.screen.blit(self.image,self.rect)
    def update(self,ai_var):
        if self.moving_right and self.rect.right < ai_var.screen_width :
            self.rect.centerx += ai_var.moving_velocity
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= ai_var.moving_velocity
        if self.moving_down and self.rect.bottom < ai_var.screen_height :
            self.rect.bottom += ai_var.moving_velocity
        if self.moving_up and self.rect.bottom > 0:
            self.rect.bottom -= ai_var.moving_velocity

class Bullet(Sprite):
    def __init__(self,ai_var,screen,ship):
        super(Bullet,self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(
            0,0,ai_var.bullet_width,ai_var.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)

        self.color = ai_var.bullet_color
        self.velocity = ai_var.bullet_velocity
    
    def update(self):
        self.y -= self.velocity
        self.rect.y = self.y
    
    def draw(self):
        pygame.draw.rect(self.screen,self.color,self.rect)

class Var():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.moving_velocity = 1.5
        self.bullet_velocity = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_maximum = 5

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
            sys.exit(0)
        check_events_key_down(ship,event,ai_var,screen,bullets)
        check_events_key_up(ship,event)

def update_screen(ai_var,screen,ship,bullets):
    screen.fill(ai_var.bg_color)
    for bullet in bullets.sprites():
        bullet.draw()
    ship.blit_me()
    pygame.display.flip()

def remove_bullets(bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def main():
    pygame.init()
    ai_var = Var()
    screen = pygame.display.set_mode(
        [ai_var.screen_width,ai_var.screen_height])
    pygame.display.set_caption("Alien War")
    ship = Ship(screen)
    bullets = Group()

    while True:                           # Game Started
        check_events(ship,ai_var,screen,bullets)             # Check events
        ship.update(ai_var)                 # Update the status of the ship
        bullets.update()  
        remove_bullets(bullets)                
        update_screen(
            ai_var,screen,ship,bullets)           # Update the screen

try:
    main()
except Exception as e:
    print("Sorry, there are some errors unexpectedly occured.")
    print(e)