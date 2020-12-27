print('''python program #25
Hashir - June 1 2018
This program is an intro do the fill tool in the turtle graphics module
''')

import turtle
t = turtle.Pen()

def hexagon(size,filled):
    if filled == True:
        t.color(1,0,1)
        t.begin_fill()
    for x in range(0,7):
        t.forward(size)
        t.left(45)
    if filled == True:
        t.end_fill()

hexagon(50,True)
