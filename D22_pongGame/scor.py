from turtle import  Turtle
ALIGNMENT = "center"
FONT = ("Arial", 50, "normal")


class ScoreBord(Turtle):
  def __init__(self):
    super().__init__()
    self.color("white")
    self.pu()
    self.ht()
    self.l_score=0
    self.r_score=0
    self.update_score()
    
  def update_score(self):
    self.clear()
    self.goto(-100,200)
    self.write(self.l_score,align=ALIGNMENT,font=FONT)
    self.goto(100,200)
    self.write(self.r_score,align=ALIGNMENT,font=FONT)
    
  def l_points(self):
    self.l_score+=1
    self.update_score()
    
  def r_points(self):
    self.r_score+=1
    self.update_score()