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

    def blit_me(self):
        self.screen.blit(self.image,self.rect)