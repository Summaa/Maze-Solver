from graphics import *
from cell import *
from maze import *

def main():
    win = Window(800, 600)
    maze = Maze(20,20, 15, 15, 20, 20, win)
    maze.create_cells()

    win.wait_for_close()

main()