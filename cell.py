import colors
from icecream import ic
from p5 import *
class Cell:
    field = None

    def __init__(self, size, x=0, y=0):
        self.color = colors.GRAY
        self.stroke_color = colors.BLACK
        self.size = size
        self.x, self.y = x, y
        self.mined = False
        self.flagged = False
        self.digged = False

    def draw(self):
        stroke(*self.stroke_color)
        fill(*self.color)
        square(self.x, self.y, self.size)
        if self.flagged:
            self.draw_flag()
        if self.field.revealed and self.mined:
            self.draw_mine()

    def draw_mine(self):
        ic()
        fill(*colors.BLACK)
        stroke(*colors.RED)
        circle(self.x, self.y, self.size, mode='CORNER')

    def draw_flag(self):
        stroke(*colors.BLACK)
        fill(*colors.RED)
        triangle(
            (self.x + 2, self.y + 2),
            (self.x + 2, self.y + self.size - 2),
            (self.x + self.size - 2, self.y + self.size / 2),
        )

    def dig(self):
        if self.flagged or self.digged:
            return True
        self.digged = True
        if self.mined:
            self.color = colors.RED
            return False
        self.color = colors.WHITE
        return True
    
    def flag(self):
        self.flagged = True
