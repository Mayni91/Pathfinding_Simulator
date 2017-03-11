from Vector2D import Vector2D
from tkinter import *


class Ball:
    canvas: Canvas = None
    x = 0
    y = 0
    maxspeed = 0

    pos: Vector2D = None
    vel: Vector2D = None
    acc: Vector2D = None

    diameter = 1
    color_fill = "white"
    color_outline = "black"
    outline_width = 2

    def __init__(self, canvas: Canvas, x, y, diameter, maxspeed, color_fill, color_outline, outline_width):
        self.canvas = canvas

        self.pos = Vector2D(x, y)
        self.vel = Vector2D()
        self.acc = Vector2D()

        self.x = x
        self.y = y
        self.diameter = diameter
        self.maxspeed = maxspeed
        self.color_fill = color_fill
        self.color_outline = color_outline
        self.outline_width = outline_width

    def setMaxSpeed(self, maxspeed):
        self.maxspeed = maxspeed

    def showBall(self):
        radius = self.diameter / 2
        x = self.pos.dx
        y = self.pos.dy
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=self.color_fill,
                                outline=self.color_outline, width=self.outline_width)

    def applyforce(self, force):
        self.acc.add(force)

    def update(self):
        self.vel.add(self.acc)
        self.vel.limit(self.maxspeed)
        self.pos.add(self.vel)
        self.acc.mult(0)

    def checkEdges(self, fieldWidth, fieldHeight):
        if (self.pos.dx > fieldWidth): self.pos.dx = 0
        if (self.pos.dx < 0): self.pos.dx = fieldWidth
        if (self.pos.dy > fieldHeight): self.pos.dy = 0
        if (self.pos.dy < 0): self.pos.dy = fieldHeight

