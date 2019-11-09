#!/usr/bin/python
import pygame
import sys
import os
from pygame.locals import *
from grid import *


class Map(Grid):
    def __init__(self, size=(10, 10, 1)):
        self.targetPos = (0, 0)
        super(Map, self).__init__(size)

    def moveTarget(self, pos):
        self.targetPos = pos

    def getRegion(self, size):
        return self.getRaw(self.targetPos, size)
