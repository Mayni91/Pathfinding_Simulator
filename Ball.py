from Vector2D import Vector2D
from tkinter import *

class Ball:

    canvas:Canvas = None
    x = 0
    y = 0
    speed = 0


    vector:Vector2D = None

    diameter = 1
    color_fill = "white"
    color_outline = "black"
    outline_width = 2

    def __init__(self, canvas:Canvas, x, y, diameter, speed, vector, color_fill, color_outline, outline_width):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.diameter = diameter
        self.speed = speed
        self.vector = vector
        self.color_fill = color_fill
        self.color_outline = color_outline
        self.outline_width = outline_width


    def setPosition(self, x, y):
        self.x = x
        self.y = y

    def addPosition(self, x, y):
        self.x += x
        self.y += y


    def setSpeed(self, speed):
        self.speed = speed

    def setVector(self, vector):
        self.vector = vector

    def showBall(self):
        radius = self.diameter/2
        x = self.x
        y = self.y
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=self.color_fill,
                                outline=self.color_outline, width=self.outline_width)


