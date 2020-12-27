print('''python program #31 - #35
Hashir - June 2 2018
#31 - This program will be the game "Bounce"
#32 - This will delay the start of the game until you right click
#33 - This will make a proper game over
#34 - This will accelerate the ball
#35 - This will record the players score
you can find the independent programs in the code mentioned by comments
''')

from tkinter import*
import random
import time

class Ball:
    def __init__(self,canvas,paddle,color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10,10,25,25, fill= color)
        self.canvas.move(self.id,245,100)
        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.score = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.hit_bottom = False
    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if(pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]):
           if(pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]):
              self.x += self.paddle.x       #accelerates the ball
              return True
        return False
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if(pos[0] <=0 ):
           self.x = 3
        if(pos[2] >=self.canvas_width) :
           self.x = -3
        if(pos[1] <= 0) :
           self.y = 3
        if(pos[3] >= self.canvas_height) :
           self.hit_bottom = True
        if(self.hit_paddle(pos) == True):
            self.score+=1
            self.y = -3

class Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10, fill = color)
        self.canvas.move(self.id,200,300)
        self.x = 0
        self.game_start=False
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
        self.canvas.bind_all('<Button-1>',self.start_game) #delays start till right click
    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos = self.canvas.coords(self.id)
        if(pos[0] <=0):
            self.x = 0
        if(pos[2] >= self.canvas_width):
            self.x = 0
    def turn_left(self,evt):
        self.x = -2
    def turn_right(self,evt):
        self.x = 2
    def start_game(self,evt):
        self.game_start = True

        
tk = Tk()
tk.title("Bounce Game")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)
canvas.pack()
tk.update()

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')
score = canvas.create_text(450,50,text = ball.score,fill = 'green',font=('Ariel',22))
                  
while True:
    if(ball.hit_bottom == False and paddle.game_start == True):
        paddle.draw()
        ball.draw()
    elif(ball.hit_bottom ==True):   #makes a proper game over
        time.sleep(0.5)
        canvas.create_text(200,200,text = "GAME OVER", fill = 'red',font = ('Ariel',32))
    tk.update_idletasks()
    canvas.itemconfig(score, text = ball.score) # records the players score
    tk.update()
    time.sleep(.01)
