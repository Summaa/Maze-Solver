from cell import *
import time

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_columns,
            cell_size_x,
            cell_size_y,
            win=None,
            ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = []
        self.create_cells()

    def create_cells(self):
        self.cells = [[Cell(self.win) for row in range(self.num_rows)] for column in range(self.num_columns)]
        for column_index, column in enumerate(self.cells):
            for row_index, cell in enumerate(column):
                self.draw_cell(column_index, row_index)

    def draw_cell(self, i, j,):
        if self.win is None:
            return
        cell = self.cells[i][j]
        x1 = self.x1 + j * self.cell_size_x
        y1 = self.y1 + i * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        cell.draw(x1, x2, y1, y2)
        self.animate()

    def break_entrance_and_exit(self):
        cell = self.cells[0][0]
        cell.has_top_wall = False
        self.draw_cell(0, 0)
        cell = self.cells[self.num_columns - 1][self.num_rows - 1]
        cell.has_bottom_wall = False
        self.draw_cell(self.num_columns - 1, self.num_rows - 1)

    def animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(.05)
