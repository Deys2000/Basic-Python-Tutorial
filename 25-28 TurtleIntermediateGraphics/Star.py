print('''python program #27
Hashir - June 1 2018
This program will use the turtle module to draw a star
depending on how you play with the angle, the star changes its sharpness
''')
import turtle
t = turtle.Pen()


def draw_star(size,points):
    for x in range(0,points*2):
        if(x%2 == 0):
            t.left(360*2/points)
            t.forward(size)
        else:
            t.right(360/points)
            t.forward(size)

draw_star(70,10)  
