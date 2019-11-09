#!/usr/bin/python

import pygame, sys, os
from pygame.locals import *
from context import *
from drawable import *

class Sprite(Drawable):
  def __init__(self, imageName, cropTopLeft, cropSize):
    self.imageName    = imageName
    self.cropTopLeft  = cropTopLeft
    self.cropSize     = cropSize

  def getImageName(self):
    return self.imageName
  
  def getArea(self):
    return self.cropTopLeft + self.cropSize

  def draw(self, context, pos):
    context.drawSprite(self, pos)