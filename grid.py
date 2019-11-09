#!/usr/bin/python
import pygame
import sys
import os
from pygame.locals import *



class Grid(object):
  def __init__(self, size):
    self.grid = []
    self.size = size
    x,y,z = size
    for ix in range(0, x):
      self.grid.append([])
      for iy in range(0, y):
        self.grid[ix].append([])
        for iz in range(0, z):
          self.grid[ix][iy].append("null")
          
  def place(self, pos, obj):
    x,y,z = pos
    self.grid[x][y][z] = obj
    
  def getRaw(self, pos, size):
    x1, y1 = pos
    sx, sy = size
    x2 = x1 + sx
    y2 = y1 + sy
    return self.grid[x1:x2][y1:y2][:]
