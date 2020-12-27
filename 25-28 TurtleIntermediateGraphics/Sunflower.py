print('''python program #26
Hashir - June 1 2018
This is not according to the book
I did program #26 along with 25 as it was an extension
This program is just me experimenting with the Turtle module
''')

import turtle
t = turtle.Pen()

t.begin_fill()
t.color(1,0,0)
t.circle(30)
t.end_fill()

t.up()
t.left(0)
t.forward(20)
t.down()

t.color(1,1,0)
for x in range(0,6):
    t.begin_fill()
    t.left(60)
    t.circle(16)
    t.end_fill()
    t.up()
    t.forward(40)
    t.down()
    
t.color(0,1,0)
for x in range(0,6):
    t.left(60)
    t.circle(16)
    t.up()
    t.forward(40)
    t.down()

