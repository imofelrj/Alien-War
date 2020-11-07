#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

import pygame.font

class Scores():
    def __init__(self,screen):
        self.score = 0
        self.screen = screen
    
    def increase(self,num):
        self.score += num
    def show_score(self):
        draw_str = "Points: " + str(self.score)
        font = pygame.font.SysFont("Times", 24)
        text = font.render(draw_str,True,(0,0,0)) # show black font
        text_rect = text.get_rect()
        text_rect.centerx = self.screen.get_rect().centerx
        text_rect.y = 10
        self.screen.blit(text,text_rect)