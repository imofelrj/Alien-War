#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

import pygame           # pygame

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