#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

from pygame.mixer import Sound

class Sounds():
    def __init__(self):
        self.bullet      = Sound("sounds/bullet.wav")
        self.enemy1_down = Sound("sounds/enemy1_down.wav")  # level 1
        self.enemy2_down = Sound("sounds/enemy2_down.wav")  # level 2
        self.enemy3_down = Sound("sounds/enemy3_down.wav")  # level 3