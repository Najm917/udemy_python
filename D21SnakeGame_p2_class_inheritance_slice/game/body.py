from turtle import Turtle
STARTINH_POSITION=[(0,0),(-20,0),(-40,0)]
move_distance=20
up=90
down=270
left=180
right=0

HEAD_COLOR   = "#FF2A55"  
BODY_COLOR_1 = "#1E1E24" 
BODY_COLOR_2 = "#E0E0E0"
   

class Snake:
  
  def __init__(self):
    self.segments=[]
    self.create_snake()
    self.head=self.segments[0]
    
  def create_snake(self):
    for position in STARTINH_POSITION:
      self.add_segment(position)
      
      
  def add_segment(self,position):
      new_segment=Turtle("circle")
      # new_segment.color(HEAD_COLOR)
      new_segment.penup()
      new_segment.goto(position)
      self.segments.append(new_segment) 
      self.style_snake()    
            
  def style_snake(self):
    for index,seg in enumerate(self.segments):
      seg.shape("circle")
      seg.shapesize(stretch_wid=0.9, stretch_len=0.9)
      if index==0:
        seg.color(HEAD_COLOR)
      elif index%2==0:
        seg.color(BODY_COLOR_2)
      else:
        seg.color(BODY_COLOR_1)
            
  def increase_body(self):
    self.add_segment(self.segments[-1].position())
    
  def move(self):
    # Body segments ko aage wale segment ki position par move karna
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
      
  
  
  # ______________________________
  
  