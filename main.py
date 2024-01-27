from graphics import *

def main():
    win = Window(800, 600)
    p1 = Point(100, 100)
    p2 = Point(500, 100)
    p3 = Point(500, 500)
    p4 = Point(100, 500)
    win.draw_line(Line(p1, p2))
    win.draw_line(Line(p2, p3))
    win.draw_line(Line(p3, p4))
    win.draw_line(Line(p4, p1))
    win.wait_for_close()

main()