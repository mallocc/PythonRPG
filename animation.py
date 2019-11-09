#!/usr/bin/python

import pygame
import sys
import os
from pygame.locals import *
from sprite import *

TICKS_MAX = 60 * 10


class Animation(Drawable):
    def __init__(self, freq):
        self.spriteFrames = []
        self.ticks = 0
        self.frame = 0
        self.freq = freq

    def addFrame(self, sprite):
        self.spriteFrames.append(sprite)

    def nextFrame(self):
        self.ticks += 1
        self.ticks = self.ticks % TICKS_MAX
        if (self.ticks % self.freq) == 0:
            self.frame += 1
            self.frame = self.frame % len(self.spriteFrames)
        return self.spriteFrames[self.frame]

    def reset(self):
        self.frame = 0
        self.ticks = 0

    def length(self):
        return len(self.spriteFrames)

    def draw(self, context, pos):
        context.drawAnimatedSprite(self, pos)
