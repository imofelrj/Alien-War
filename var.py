#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

# var.py
"""
    This file is used for some constant variables
"""

class Var():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.moving_velocity = 3
        self.bullet_velocity = 6
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_maximum = 5
        self.alien_maximum = 7
        self.alien_velocity = 1
        self.alien_points = 10