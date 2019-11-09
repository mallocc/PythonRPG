#!/usr/bin/python
import pygame
import sys
import os
from pygame.locals import *

from entity import *

class Player(Entity):
    def __init__(self, pos, drawable):
        super(Player, self).__init__(pos, drawable)