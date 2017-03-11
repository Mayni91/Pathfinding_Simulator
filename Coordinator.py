from Field import Field
from MeshGrid import MeshGrid
from Vector2D import Vector2D
from Ball import Ball
from tkinter import *


class Coordinator:

    top = None
    field = None
    meshGrid = None
    canvas: Canvas = None
    ball: Ball = None

    meshgridEnabled = False
    footballfieldEnabled = True

    def __init__(self):
        self.top = Tk()
        self.canvas = Canvas(self.top, bg="darkgreen", height=700, width=1000)
        self.field = Field(self.canvas, "darkgreen", 1000, 700, 50, 30, 160, 80,150, 70, 200, 10, 150, 5)
        self.meshGrid = MeshGrid(self.canvas, 1000, 700, 50, 15)
        self.ball = Ball(self.canvas, 500, 350, 10, 0, (Vector2D(0, 0)), "white", "black", 1)

        buttonNextFrame = Button(self.top, text="Next Frame", command=self.nextFrame)
        buttonNextFrame.place(x=350, y=680)

        buttonShowMeshgrid = Button(self.top, text="Show Grid", command=self.showMeshGrid)
        buttonShowMeshgrid.place(x=550, y=680)

        buttonShowField = Button(self.top, text="Show Field", command=self.showFootballField)
        buttonShowField.place(x=450, y=680)

        self.nextFrame()
        self.canvas.pack()
        self.top.mainloop()

    def nextFrame(self):
        print("invalidate test")
        self.canvas.delete("all")
        if self.footballfieldEnabled:
            self.canvas.config(bg="darkgreen")
            self.field.showField()
        else:
            self.canvas.config(bg="white")

        self.ball.addPosition(5, 5)
        self.ball.showBall()
        if self.meshgridEnabled:
            self.meshGrid.showGrid()


    def showMeshGrid(self):
        self.meshgridEnabled = not  self.meshgridEnabled
        self.nextFrame()

    def showFootballField(self):
        self.footballfieldEnabled = not self.footballfieldEnabled
        self.nextFrame()
