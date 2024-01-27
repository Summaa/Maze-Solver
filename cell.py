from graphics import *

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None
        self.win = win
    
    def draw(self, x1, x2, y1, y2):
        if self.win is None:
            return
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.win.draw_line(line)

    def draw_move(self, to_cell, undo=False):
        if self.win is None:
            return
        x_mid = (self.x1 + self.x2) / 2
        y_mid = (self.y1 + self.y2) / 2
        to_x_mid = (to_cell.x1 + to_cell.x2) / 2
        to_y_mid = (to_cell.y1 + to_cell.y2) / 2

        fill_color = "red"
        if undo:
            fill_color = "grey"

        #left
        if self.x1 > to_cell.x1:
            line = Line(Point(self.x1, y_mid), Point(x_mid, y_mid))
            self.win.draw_line(line, fill_color)
            line = Line(Point(to_cell.x2, to_y_mid), Point(to_x_mid, to_y_mid))
            self.win.draw_line(line, fill_color)
        #right
        if self.x1 < to_cell.x1:
            line = Line(Point(self.x2, y_mid), Point(x_mid, y_mid))
            self.win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_y_mid), Point(to_cell.x1, to_y_mid))
            self.win.draw_line(line, fill_color)
        #up
        if self.y1 > to_cell.y1:
            line = Line(Point(x_mid, self.y1), Point(x_mid, y_mid))
            self.win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_cell.y2), Point(to_x_mid, to_y_mid))
            self.win.draw_line(line, fill_color)
        #down
        if self.y1 < to_cell.y1:
            line = Line(Point(x_mid, self.y2), Point(x_mid, y_mid))
            self.win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_cell.y1), Point(to_x_mid, to_y_mid))
            self.win.draw_line(line, fill_color)
