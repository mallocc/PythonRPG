#!/usr/bin/python

import pygame
import sys
import os
import json
from pygame.locals import *
from sprite import *
from animation import *
from copy import deepcopy

NULL_TEX = "nulltex.png"

IMAGE_DATABASE = "images.json"


class ImageManager:
    def __init__(self):
        self.images = {}
        self.sprites = {}
        self.animations = {}
        self.importImages(IMAGE_DATABASE)
        self.importSprites(IMAGE_DATABASE)
        self.importAnimations(IMAGE_DATABASE)

    def importImages(self, filename):
        with open(filename) as json_file:
            data = json.load(json_file)
            for image in data["images"]:
                self.addImage(image["name"], image["path"])

    def importSprites(self, filename):
        with open(filename) as json_file:
            data = json.load(json_file)
            for sprite in data["sprites"]:
                name = sprite["name"]
                imageName = sprite["imageName"]
                positionData = sprite["position"]
                pos = (positionData["x"], positionData["y"])
                sizeData = sprite["size"]
                size = (sizeData["x"], sizeData["y"])
                self.addSprite(name, imageName, pos, size)

    def importAnimations(self, filename):
        with open(filename) as json_file:
            data = json.load(json_file)
            for animation in data["animations"]:
                name = animation["name"]
                freq = animation["frequency"]
                ani = Animation(freq)
                for frame in animation["frames"]:
                    ani.addFrame(self.getSprite(frame))
                self.addAnimation(name, ani)                

    def addImage(self, name, path):
        self.images[name] = pygame.image.load(path)

    def addSprite(self, name, imageName, pos, size):
        self.sprites[name] = Sprite(imageName, pos, size)

    def addAnimation(self, name, animation):
        self.animations[name] = animation

    def getImage(self, name):
        return self.images[name]

    def getSprite(self, name):
        return self.sprites[name]

    def getAnimation(self, name):
        return self.animations[name]
    
    def getImageDup(self, name):
        return deepcopy(self.images[name])

    def getSpriteDup(self, name):
        return deepcopy(self.sprites[name])

    def getAnimationDup(self, name):
        return deepcopy(self.animations[name])
