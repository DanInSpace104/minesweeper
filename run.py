from itertools import product

import p5 as p

world = {}


class Cell:
    def __init__(self, size, x=0, y=0):
        self.size = size
        self.x, self.y = x, y

    def draw(self):
        p.rect(self.x, self.y, self.size)


def setup():
    border = 5
    cell_size = 10
    cell_horizontal_num = 8
    cell_vertical_num = 8
    p.size(
        border * 2 + cell_size * cell_horizontal_num,
        border * 2 + cell_size * cell_vertical_num,
    )
    p.no_loop()

    field = [
        [Cell(cell_size, i * cell_size, j * cell_size)]
        for i, j in product(range(cell_size), repeat=2)
    ]
    for x, y in product(range(cell_size), repeat=2):
        field[x][y].draw()


def draw():
    pass
    # p.


p.run()
# if __name__ == '__main__':
#     p.run()
