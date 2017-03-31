from MathLib import Vector2
import steeringapp
import gametemplate
import math
import random
import os

class Agent(object):
    def __init__(self, pos, maxvel):
        self.velocity = Vector2(1, 1)
        self.heading = Vector2(0, 0)
        self.position = pos
        self.maxvelocity = maxvel        
        self.force = Vector2(0, 0)
        self._choice_ = None
        self.wanderangle = math.pi / 4.0

    def seek(self, target):
        tmp = target.position - self.position
        v = tmp.Normalize() * self.maxvelocity
        seekforce = v - self.velocity
        return seekforce
    
    
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
        wanderangle = self.wanderangle + (random.random() * 1) - (1 * .5)
        dispacement.VecX = math.cos(wanderangle) * dispacement.Magnitude()
        dispacement.VecY = math.sin(wanderangle) * dispacement.Magnitude()
        os.system("cls")       
        print dispacement 
        return dispacement
        
    def update(self, deltatime, target):
        if self._choice_ is None or self._choice_ is 0:
            self.force = self.idle(deltatime)

        if self._choice_ is 1:
            self.force = self.seek(target)

        if self._choice_ is 2:
            self.force = self.flee(target)
        
        if self._choice_ is 3:
            self.force = self.wander(25, 10)
        
        
        acceleration = self.force * (1 / 1)
        self.velocity = self.velocity + (acceleration * deltatime)
        if self.velocity.Magnitude() > self.maxvelocity:
            self.velocity = self.velocity.Normalize()
        self.position = self.position + (self.velocity * deltatime)
        self.heading = self.velocity.Normalize()
        
        
