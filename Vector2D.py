import math as math
import random as random

class Vector2D:

    dx = 0
    dy = 0

    def __init__(self, dx=0, dy=0):
        self.dx = dx
        self.dy = dy

    def print(self):
        print("Vector2D(x: " + self.dx + ", y: " + self.dy + ")")

    def normalize(self):
        self.dx /= self.mag()
        self.dy /= self.mag()

    def limit(self, maxvalue):
        magsquared = math.pow(self.mag(), 2)

        if (magsquared > maxvalue * maxvalue) & (magsquared > 0):
            ratio = maxvalue / math.sqrt(magsquared)
            self.mult(ratio)

    def mag(self):
        return math.sqrt(self.dx * self.dx + self.dy * self.dy)

    def mult(self, factor):
        self.dx *= factor
        self.dy *= factor

    def add(self, vector):
        self.dx += vector.dx
        self.dy += vector.dy
        #return Vector2D(self.dx + vector.dx, self.dy + vector.dy)

    def sub(self, vector):
        self.dx -= vector.dx
        self.dy -= vector.dy
        #return Vector2D(self.dx - vector.dx, self.dy - vector.dy)

    def div(self, factor):
        self.dx /= factor
        self.dy /= factor

    def dot(self, vector):
        return self.dx * vector.dx + self.dy * vector.dy

    def anglebetween(self, vector):
        return math.atan2(vector.dx - self.dx, self.dy - vector.dy)

    def random2D(self):
        return Vector2D(random.uniform(-1, 1), random.uniform(-1,1))