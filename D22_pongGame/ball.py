from turtle import Turtle
import random
class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.color("white")
    self.pu()
    self.x_move=10
    self.y_move=10
    self.move_speed=0.1
    
    
  def random_move(self):
    random_x=self.xcor()+self.x_move
    random_y=self.ycor()+self.y_move
    self.goto(random_x,random_y)
    
  def boune_ball_y(self):
    self.y_move*=-1
    
  def boune_x_paddle(self):
    self.x_move*=-1
    # incress speed
    self.move_speed*0.9
    
    
  def miss_ball(self):
    self.goto(0,0)
    self.move_speed=0.1
    self.boune_x_paddle()