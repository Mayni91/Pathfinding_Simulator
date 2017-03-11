from tkinter import *

class MeshGrid:

    canvas = None
    height = 0
    width = 0
    border = 0
    gridWidth = 0


    field_top = 0
    field_bottom = 0
    field_left = 0
    field_right = 0

    def __init__(self, canvas:Canvas, width, height, border, gridWidth):
        self.canvas = canvas
        self.height = height
        self.width = width
        self.border = border
        self.gridWidth = gridWidth

        self.field_top = border
        self.field_bottom = height - border
        self.field_left = border
        self.field_right = width - border

        return

    def showGrid(self):
        self.__drawBorder()
        self.__drawLines()


    def __drawBorder(self):

        self.canvas.create_rectangle(self.field_left,self.field_top,self.field_right,self.field_bottom, outline="black", width="1")

    def __drawLines(self):
        for i in range(self.field_top, self.field_bottom, self.gridWidth):
            self.canvas.create_line(self.field_left, i , self.field_right, i, fill="black", width="1")

        for i in range(self.field_left, self.field_right, self.gridWidth):
            self.canvas.create_line(i, self.field_top, i, self.field_bottom, fill="black", width="1")
