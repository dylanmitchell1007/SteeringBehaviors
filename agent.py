from MathLib import Vector2
import steeringapp
import gametemplate
import math
import pygame
import random
import os


class Agent(object):
    def __init__(self, pos, maxvel):
        self.velocity = Vector2(1, 1)
        self.heading = Vector2(0, 0)
        self.position = pos
        self.maxvelocity = maxvel
        self.force = Vector2(0, 0)
        self._choice_ = 0
        self.wanderangle = math.pi / 4.0
        self.previousangle = math.pi / 4.0
        self.color = (255, 0, 0)

    def seek(self, target):
        tmp = target.position - self.position
        v = tmp.Normalize() * self.maxvelocity
        seekforce = v - self.velocity
        return seekforce

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, [int(
            self.position.GetX()), int(self.position.GetY())], 40)

    def flee(self, target):
        fle = self.position - target.position
        f = fle.Normalize() * self.maxvelocity
        fleeforce = f - self.velocity
        return fleeforce

    def idle(self, deltatime):
        accel = self.velocity * deltatime
        self.heading = self.velocity.Normalize()
        return accel

    def wander(self, distance, radius):
        center_circle = self.velocity.Normalize()
        center_circle = center_circle * distance
        dispacement = Vector2(0, 1) * radius
        deltaangle = self.previousangle - self.wanderangle
        newangle = (random.randrange(0.0, 1.0) *
                    deltaangle) - (deltaangle * .5)
        self.previousangle = newangle
        self.wanderangle += newangle

        dispacement.VecX = math.cos(self.wanderangle) * dispacement.Magnitude()
        dispacement.VecY = math.sin(self.wanderangle) * dispacement.Magnitude()
        
        return dispacement

    def update(self, deltatime, target):
        if self._choice_ is None or self._choice_ is 0:
            self.force = self.idle(deltatime)

        if self._choice_ is 1:
            self.force = self.seek(target)

        if self._choice_ is 2:
            self.force = self.flee(target)

        if self._choice_ is 3:
            self.force = self.wander(500, 300)

        acceleration = self.force * (1 / 1)
        self.velocity = self.velocity + (acceleration * deltatime)
        if self.velocity.Magnitude() > self.maxvelocity:
            self.velocity = self.velocity.Normalize()
        self.position = self.position + (self.velocity * deltatime)
        self.heading = self.velocity.Normalize()
