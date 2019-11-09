#!/usr/bin/python
import pygame
import sys
import os
from pygame.locals import *
from entity import *

from math import sqrt
from random import randint
from globals import *


class NPC(Entity):
    def __init__(self, pos, drawable, static=True, followPlayer=False):
        self.moveTarget = (0, 0)
        self.speed = 1
        self.attentionSpan = 1
        self.attentionCount = 0
        self.static = static
        self.followPlayer = followPlayer
        super(NPC, self).__init__(pos, drawable)

    def updateAttention(self):
        self.attentionCount += 1
        if (self.attentionCount % self.attentionSpan) == 0:
            self.attentionSpan = randint(30, 100)
            self.attentionCount = 0
            self.moveTarget = (randint(0, R600[0]), randint(0, R600[1]))

    def updateMove(self):
        x1, y1 = self.pos
        x2, y2 = self.moveTarget
        dx, dy = (x2 - x1, y2 - y1)
        d = sqrt(dx*dx + dy*dy) + 1
        dx = dx / d
        dy = dy / d
        self.vel = (dx * self.speed, dy * self.speed)

    def update(self, friction):
        if not self.static and not self.followPlayer:
            self.updateAttention()
            self.updateMove()
        super(NPC, self).update(friction)

    def npcUpdate(self, player):
        if not self.static and self.followPlayer:
            self.moveTarget = player.pos
            self.updateMove()
