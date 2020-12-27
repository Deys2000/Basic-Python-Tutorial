print('''python program #28
Hashir - June 1 2018
This program is an intro to TKINTER module
It will display lots of multicolored triangles
''')

from tkinter import*
import random

tk = Tk()
canvas = Canvas(tk,width=450,height=450)
canvas.pack()
colors = ['blue','red','green','cyan','yellow','black','magenta','orange','purple']

def create_triangle():
    locationX1 = random.randrange(450)
    locationY1 = random.randrange(450)
    locationX2 = random.randrange(450)
    locationY2 = random.randrange(450)
    locationX3 = random.randrange(450)
    locationY3 = random.randrange(450)
    color = random.choice(colors)    
    canvas.create_polygon(locationX1,locationY1,locationX2,locationY2,locationX3,locationY3,fill=color,outline="black")

for x in range(0,100):
    create_triangle()
