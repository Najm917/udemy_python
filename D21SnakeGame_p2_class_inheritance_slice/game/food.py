from turtle import Turtle,Screen
import random,time

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
    
    
class SpecialFood(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(1.2, 1.2)        # Regular food se bada
        self.color("#FFD700")            # Glowing Gold
        self.speed("fastest")
        self.hideturtle()                # Shuruat me hidden rahega
        self.is_active = False
        self.spawn_time = 0

    def spawn(self):
        random_x = random.randint(-250, 250)
        random_y = random.randint(-250, 250)
        self.goto(random_x, random_y)
        self.showturtle()
        self.is_active = True
        self.spawn_time = time.time()    # Current time note karna

    def disappear(self):
        self.hideturtle()
        self.goto(1000, 1000)            # Screen se door bhej do
        self.is_active = False