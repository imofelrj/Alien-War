#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

import pygame
from random import randrange
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,screen,ai_var):
        super(Alien,self).__init__()
        self.screen = screen
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        self.velocity = ai_var.alien_velocity
        self.rect.x = randrange(0,ai_var.screen_width)
        self.rect.y = randrange(-ai_var.screen_height // 4,0)
    
    def draw(self):
        self.screen.blit(self.image,self.rect)
    def update(self):
        self.rect.y += self.velocity