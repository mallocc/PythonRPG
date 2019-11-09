#!/usr/bin/python

from sprite import Drawable


class Entity(object):
    def __init__(self, pos, drawable):
        self.pos = pos
        self.vel = (0, 0)
        self.drawable = drawable

    def update(self, friction=1):
        self.vel = (self.vel[0] * friction, self.vel[1] * friction)
        self.pos = (self.pos[0] + self.vel[0], self.pos[1] + self.vel[1])

    def draw(self, context):
        self.drawable.draw(context, self.pos)
