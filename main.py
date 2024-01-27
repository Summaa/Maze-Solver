from graphics import *
from cell import *

def main():
    win = Window(800, 600)
    cell1 = Cell(win)
    cell1.has_left_wall = False
    cell1.draw(100, 150, 100, 150)

    cell2 = Cell(win)
    cell2.has_top_wall = False
    cell2.draw(100, 150, 151, 201)

    cell3 = Cell(win)
    cell3.has_right_wall = False
    cell3.draw(151, 201, 100, 150)

    cell4 = Cell(win)
    cell4.has_bottom_wall = False
    cell4.draw(151, 201, 151, 201)

    cell1.draw_move(cell2)
    cell2.draw_move(cell4, True)

    win.wait_for_close()

main()