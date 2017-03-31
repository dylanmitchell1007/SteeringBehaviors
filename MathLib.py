import math

class Vector2(object):

    def __init__(self, xpos, ypos):
        self.VecX = xpos
        self.VecY = ypos
        
    def __add__(self, other):
        return Vector2 (self.VecX + other.VecX, self.VecY + other.VecY)

    def __sub__(self, other):
        return Vector2 (self.VecX - other.VecX, self.VecY - other.VecY)

    def __mul__(self, other):
        return Vector2 (self.VecX * other, self.VecY * other)
        
    def Magnitude( self):
        return math.sqrt((self.VecX * self.VecX) + (self.VecY * self.VecY))

    def Normalize(self):
        if self.Magnitude() <= 0:
            return Vector2(0,0)
        return Vector2(self.VecX  / self.Magnitude(), self.VecY / self.Magnitude())

    def __str__(self):
        return "<" + str(self.GetX()) +  "," + str(self.GetY()) + ">"

    def DotProd(self, dotprod):
        return (self.VecX * self.VecX) + (self.VecY * self.VecY)

    def GetY(self):
        return self.VecY
    def GetX(self):
        return self.VecX

test = Vector2(0, 2)
test2 = Vector2(1,1)
Sum = test + test2
print Sum
