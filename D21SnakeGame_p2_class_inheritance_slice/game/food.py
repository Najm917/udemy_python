from turtle import Turtle,Screen
import random

class Foood(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.penup()
    self.shapesize(0.5,0.5)
    self.color("#FFD166")
    self.speed("fast")
    self.refresh()
    
  def refresh(self):
    random_x=random.randint(-280,280)
    random_y=random.randint(-280,280)
    self.goto(random_x,random_y)
    