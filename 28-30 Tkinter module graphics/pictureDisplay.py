print('''python program # 30
Hashir - June 2 2018
This program will import a gif picture and move it
''')
import time
from tkinter import*
tk = Tk()

canvas = Canvas(tk,width=500,height=700)
canvas.pack()
my_image = PhotoImage(file='c:\\Users\\aquadri\\Desktop\\animated.gif')
c = canvas.create_image(0,0, anchor=NW, image = my_image)

for x in range(0,10):
    canvas.move(c,5,0)
    tk.update()
    time.sleep(.25)
