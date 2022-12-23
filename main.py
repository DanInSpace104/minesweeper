# flake8: noqa
# pyright: ignore
from itertools import product

import p5 as p
from icecream import ic
# import p5 as p
from p5 import *

import colors
from cell import Cell

mine_number = 10
border = 5
bg_color = colors.BLACK
cell_size = 20
cell_horizontal_num = 9
cell_vertical_num = 9
rhc = range(cell_horizontal_num)
rvc = range(cell_horizontal_num)


DIG_KEY = 'h'
FLAG_KEY = 't'


class Field(list):
    revealed = False
    mine_num = mine_number

    def reveal(self):
        self.revealed = True
        ic()
        # for i in rhc:
        #     for j in rvc:
        #         self[i][j].reveal()
        no_loop()

    def draw(self):
        for i in rhc:
            for j in rvc:
                self[i][j].draw()

    def by_coords(self, x, y):
        return self[(int(y) - border) // cell_size][(int(x) - border) // cell_size]

    def check_win(self):
        undigged = len(
            [self[x][y] for x, y in product(rhc, rvc) if not self[x][y].digged]
        )
        if undigged == self.mine_num:
            raise Exception('ABSOLUTE WIN')


field = Field()


def setup():
    size(
        border * 2 + cell_size * cell_horizontal_num,
        border * 2 + cell_size * cell_vertical_num,
    )
    Cell.field = field
    for j in rvc:
        field.append(
            [Cell(cell_size, i * cell_size + border, j * cell_size + border) for i in rhc]
        )

    field[2][2].mined = True
    field[1][2].mined = True


def draw():
    background(*bg_color)
    field.draw()


def key_pressed():
    if key == 'q':
        exit()
    elif key == DIG_KEY:
        if field.by_coords(mouse_x, mouse_y).dig():
            pass
        else:
            field.reveal()
    elif key == FLAG_KEY:
        field.by_coords(mouse_x, mouse_y).flag()
    field.check_win()


if __name__ == '__main__':
    run()
