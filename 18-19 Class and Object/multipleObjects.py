print('''Python program #19
Hashir - May 30 2018
This program draws a pitchfork, its using multiple objects of a single class
''')
import turtle

lineOne = turtle.Pen()
lineTwo = turtle.Pen()
lineThree = turtle.Pen()
lineFour = turtle.Pen()

lineOne.forward(100)
lineTwo.forward(100)
lineThree.forward(100)
lineFour.forward(100)

lineOne.left(90)
lineTwo.left(90)
lineThree.right(90)
lineFour.right(90)

lineOne.forward(40)
lineTwo.forward(20)
lineThree.forward(20)
lineFour.forward(40)

lineOne.right(90)
lineTwo.right(90)
lineThree.left(90)
lineFour.left(90)

lineOne.forward(40)
lineTwo.forward(40)
lineThree.forward(40)
lineFour.forward(40)
