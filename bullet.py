#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

import pygame
from pygame.sprite import Sprite

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