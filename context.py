#!/usr/bin/python

import pygame
import sys
import os
from pygame.locals import *
from sprite import *
from animation import *
from imagemanager import *
from map import *
from globals import *

class Context:
    def __init__(self, bgColor, windowSize, fps, title):
        pygame.init()
        self.windowSize = windowSize
        self.bgColor = bgColor
        self.fps = fps
        self.fpsClock = pygame.time.Clock()
        self.surface = pygame.display.set_mode(windowSize)
        self.setTitle(title)
        self.imageManager = ImageManager()
        self.map = Map()

    def startDraw(self):
        self.surface.fill(self.bgColor)

    def endDraw(self):
        pygame.display.update()
        self.fpsClock.tick(self.fps)

    def getSurface(self):
        return self.surface

    def setTitle(self, title):
        pygame.display.set_caption(title)

    def setBackground(self, color):
        self.bgColor = color

    def drawImage(self, image, pos, area=None):
        if isinstance(image, pygame.Surface):
            self.surface.blit(image, pos, area)
        elif isinstance(image, str):
            self.drawImage(self.imageManager.getImage(image),
                           pos,
                           area)

    def drawSprite(self, sprite, pos):
        self.drawImage(
            self.imageManager.getImage(sprite.getImageName()),
            pos,
            sprite.getArea())

    def drawAnimatedSprite(self, animatedSprite, pos):
        self.drawSprite(animatedSprite.nextFrame(), pos)

    def moveMapTarget(self, pos):
        self.map.moveTarget(pos)

    def drawMap(self, size):
        sx = min(size[0], max(0, self.map.size[0]))
        sy = min(size[1], max(0, self.map.size[1]))
        sz = self.map.size[2]
        region = self.map.getRegion(size)
        for x in range(0, sx):
            for y in range(0, sy):
                for z in range(0, sz):
                    imageName = region[x][y][z]
                    self.drawImage(imageName, (x * 64, y * 64))
