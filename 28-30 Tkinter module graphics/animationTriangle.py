print('''python program #29
Hashir - June 1 2018
This is my intro to animation
I create a triangle and send it across the borders of the canvas
''')

import time
from tkinter import*
tk = Tk()
canvas = Canvas(tk,width=400,height=400)
canvas.pack()
triangle = canvas.create_polygon(10,10,10,60,50,35)

for x in range(0,60):
    canvas.move(triangle,5,0)
    tk.update()
    time.sleep(.05)

for x in range(0,60):
    canvas.move(triangle,0,5)
    tk.update()
    time.sleep(.05)

for x in range(0,60):
    canvas.move(triangle,-5,0)
    tk.update()
    time.sleep(.05)

for x in range(0,60):
    canvas.move(triangle,0,-5)
    tk.update()
    time.sleep(.05)
