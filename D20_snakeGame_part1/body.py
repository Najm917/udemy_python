from turtle import Turtle
STARTINH_POSITION=[(0,0),(-20,0),(-40,0)]
move_distance=20
up=90
down=270
left=180
right=0
class Snake:
  
  
  def __init__(self):
    self.segments=[]
    self.create_snake()
    self.head=self.segments[0]
    
  def create_snake(self):
    for position in STARTINH_POSITION:
      new_segment=Turtle("square")
      new_segment.color("white")
      new_segment.penup()
      new_segment.goto(position)
      self.segments.append(new_segment)
      
      
  def move(self):
    for seg_num in range(len(self.segments)-1,0,-1):
        new_x=self.segments[seg_num-1].xcor()
        new_y=self.segments[seg_num-1].ycor()
        self.segments[seg_num].goto(new_x,new_y)
    self.segments[0].forward(move_distance)
    
  def move_up(self):
    if self.head.heading()!=down:
      self.head.setheading(up)
  def move_down(self):
    if self.head.heading()!=up:
      self.head.setheading(down)
  def move_left(self):
    if self.head.heading()!=right:
      self.head.setheading(left)
  def move_right(self):
    if self.head.heading()!=left:
      self.head.setheading(right)
    