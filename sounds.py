#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

from pygame.mixer import Sound

class Sounds():
    def __init__(self):
        self.bullet = Sound("sounds/bullet.wav")
    