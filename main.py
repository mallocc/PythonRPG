#!/usr/bin/python
import pygame
import sys
import os
from pygame.locals import *
from context import *
from imagemanager import *
from sprite import *
from animation import *
from entity import *
from player import *
from npc import *

from random import randint


class Game:
    def __init__(self):
        self.context = Context(MAGENTA, R600, 60, "Game")
        self.room = (0, 0)
        self.player = Player(
            (0, 0), self.context.imageManager.getAnimationDup("redSprite"))
        self.entities = []

    def addEntity(self, entity):
        self.entities.append(entity)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            self.player.vel = (self.player.vel[0], self.player.vel[1] - 1)
        if keys[K_DOWN]:
            self.player.vel = (self.player.vel[0], self.player.vel[1] + 1)
        if keys[K_RIGHT]:
            self.player.vel = (self.player.vel[0] + 1, self.player.vel[1])
        if keys[K_LEFT]:
            self.player.vel = (self.player.vel[0] - 1, self.player.vel[1])

        self.player.update(0.85)
        for ent in self.entities:
            ent.update(0.85)
            if isinstance(ent, NPC):
                ent.npcUpdate(self.player)

    def draw(self):
        self.context.startDraw()

        self.context.drawMap((11, 11))
        
        self.player.draw(self.context)
        for ent in self.entities:
            ent.draw(self.context)

        self.context.endDraw()


game = Game()
game.addEntity(NPC((0, 0), game.context.imageManager.getAnimationDup(
    "greenSprite"), False, True))
game.addEntity(
    NPC((0, 0), game.context.imageManager.getAnimationDup("redSprite"), False))

### Main loop ###
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    game.update()
    game.draw()

#################
