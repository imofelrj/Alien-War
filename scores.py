#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

import pygame.font

class Scores():
    def __init__(self,screen,ai_var):
        self.score = 0
        self.screen = screen
        self.killed = 0
        self.level = 1
        self.ship_left = ai_var.ship_limit
        self.bullets_left = ai_var.bullets_limit
        self.game_active = True
    def show_score(self):
        draw_str = "Points: " + str(self.score)
        font = pygame.font.SysFont("Times", 24)
        text = font.render(draw_str,True,(0,0,0)) # show black font
        text_rect = text.get_rect()
        text_rect.centerx = self.screen.get_rect().centerx * 0.9
        text_rect.y = 10
        self.screen.blit(text,text_rect)
    def show_ship_num(self):
        draw_str = "Ships: " + str(self.ship_left)
        font = pygame.font.SysFont("Times", 24)
        text = font.render(draw_str,True,(0,0,0)) # show black font
        text_rect = text.get_rect()
        text_rect.centerx = self.screen.get_rect().centerx * 1.3
        text_rect.y = 10
        self.screen.blit(text,text_rect)
    def show_level(self):
        self.level = 1 + self.killed // 20
        draw_str = "Level: " + str(self.level)
        font = pygame.font.SysFont("Times", 24)
        text = font.render(draw_str,True,(0,0,0)) # show black font
        text_rect = text.get_rect()
        text_rect.centerx = self.screen.get_rect().centerx * 1.1
        text_rect.y = 10
        self.screen.blit(text,text_rect)
    def show_bullets_num(self):
        draw_str = "Bullets: " + str(self.bullets_left)
        font = pygame.font.SysFont("Times", 24)
        text = font.render(draw_str,True,(0,0,0)) # show black font
        text_rect = text.get_rect()
        text_rect.centerx = self.screen.get_rect().centerx * 0.7
        text_rect.y = 10
        self.screen.blit(text,text_rect)