from tkinter import *

class Field:

    canvas = None
    backgroundColor = "darkgreen"
    lengthX = 0
    lengthY = 0
    border = 0
    goalWidth = 0
    goalHeight = 0
    centerCircleDiameter = 0
    penaltyWidth = 0
    penaltyHeight = 0
    penaltyCrossSize = 0
    penaltyCrossDistance = 0
    pillarDistanceFromMiddle = 0
    lineColour = "white"
    widthLines = 1

    field_top = 0
    field_bottom = 0
    field_left = 0
    field_right = 0


    def __init__(self, canvas:Canvas, backgroundColor, lengthX, lengthY, border, goalWidth, goalHeight, pillarDistanceFromMiddle,  centerCircleDiameter, penaltyWidth, penaltyHeight, penaltyCrossSize, penaltyCrossDistance,widthLines):
        self.canvas = canvas
        self.backgroundColor = backgroundColor
        self.lengthX = lengthX
        self.lengthY = lengthY
        self.border = border
        self.goalWidth = goalWidth
        self.goalHeight = goalHeight
        self.pillarDistanceFromMiddle = pillarDistanceFromMiddle
        self.centerCircleDiameter = centerCircleDiameter
        self.penaltyWidth = penaltyWidth
        self.penaltyHeight = penaltyHeight
        self.widthLines = widthLines
        self.penaltyCrossSize = penaltyCrossSize
        self.penaltyCrossDistance = penaltyCrossDistance

        self.field_top = border
        self.field_bottom = lengthY - border
        self.field_left = border
        self.field_right = lengthX - border

    def showField(self):
        self.__drawField()

    def __drawField(self):
        self.__drawFieldBorder()
        self.__drawGoals()
        self.__drawMiddleLine()
        self.__drawMiddleCircle()
        self.__drawPenaltyZones()
        self.__drawPillars()

    def draw_rectange(self, tl, tr, br, bl, color, widthLine):

        self.canvas.create_line(tl, tr, br, bl, tl, tr, fill=color, width=widthLine)
        return

    def draw_circle(self, tl, br, color, widthLine):
        self.canvas.create_oval(tl, br, outline=color, width=widthLine)
        return

    def draw_pillar(self, x, y, color, widthLine):
        self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=color, outline=color, width=widthLine)
        return

    def draw_cross(self, x, y, length, color, widthLine):
        self.canvas.create_line(x - length / 2, y, x + length / 2, y, fill=color, width=widthLine)
        self.canvas.create_line(x, y - length / 2, x, y + length / 2, fill=color, width=widthLine)
        return


    def __drawFieldBorder(self):
        top_Left = self.field_left, self.field_top
        bottom_Right = self.field_right, self.field_bottom
        self.canvas.create_rectangle(top_Left, bottom_Right, width=self.widthLines, outline="white")
        return

    def __drawGoals(self):
        middleY = self.lengthY / 2

        # Left Goal
        top_Left = self.field_left - self.goalWidth, middleY - self.goalHeight/2
        bottom_Right = self.field_left , middleY + self.goalHeight/2
        self.canvas.create_rectangle(top_Left, bottom_Right, width=self.widthLines, outline="white")

        # Right Goal
        top_Left = self.field_right, middleY - self.goalHeight / 2
        bottom_Right = self.field_right + self.goalWidth, middleY + self.goalHeight / 2
        self.canvas.create_rectangle(top_Left, bottom_Right, width=self.widthLines, outline="white")
        return

    def __drawMiddleLine(self):
        middleX = self.lengthX / 2
        self.canvas.create_line(middleX, self.field_top, middleX, self.field_bottom, width=self.widthLines, fill="white")
        return

    def __drawMiddleCircle(self):
        # middle Circle
        radius = self.centerCircleDiameter/2
        middle_topleft = self.lengthX /2 - radius, self.lengthY /2 - radius
        middle_bottomright = self.lengthX / 2 + radius, self.lengthY / 2 + radius
        self.draw_circle(middle_topleft, middle_bottomright, "white", self.widthLines)

        # middle cross
        self.draw_cross(self.lengthX / 2, self.lengthY / 2, self.penaltyCrossSize, color="white", widthLine=self.widthLines)

        return

    def __drawPenaltyZones(self):

        # left penalty
        topLeft = self.field_left, self.lengthY/2 - self.penaltyHeight/2,
        bottomRight = self.field_left + self.penaltyWidth ,self.lengthY/2 + self.penaltyHeight / 2
        self.canvas.create_rectangle(topLeft, bottomRight, width=self.widthLines, outline="white")

        # right penalty
        topLeft = self.field_right - self.penaltyWidth, self.lengthY / 2 - self.penaltyHeight / 2,
        bottomRight = self.field_right, self.lengthY / 2 + self.penaltyHeight / 2
        self.canvas.create_rectangle(topLeft, bottomRight, width=self.widthLines, outline="white")

        # penatly cross's

        leftPenaltyCross = self.field_left + self.penaltyCrossDistance
        self.draw_cross(leftPenaltyCross, self.lengthY/2,self.penaltyCrossSize, color="white", widthLine=self.widthLines)
        rightPenaltyCross = self.field_right - self.penaltyCrossDistance
        self.draw_cross(rightPenaltyCross, self.lengthY/2,self.penaltyCrossSize, color="white", widthLine=self.widthLines)
        return

    def __drawPillars(self):
        middle_Y = self.lengthY / 2

        #left pillars
        self.draw_pillar(self.field_left, middle_Y - self.pillarDistanceFromMiddle, color="white", widthLine=self.widthLines)
        self.draw_pillar(self.field_left, middle_Y + self.pillarDistanceFromMiddle, color="white", widthLine=self.widthLines)

        # right pillars
        self.draw_pillar(self.field_right, middle_Y - self.pillarDistanceFromMiddle, color="white", widthLine=self.widthLines)
        self.draw_pillar(self.field_right, middle_Y + self.pillarDistanceFromMiddle, color="white", widthLine=self.widthLines)
        return
