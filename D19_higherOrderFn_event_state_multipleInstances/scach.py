from turtle import Turtle,Screen

timmy=Turtle()
screen=Screen()
screen.listen()

def forward():
  timmy.forward(10)
  timmy.color("red")
  timmy.pensize(8)
  
def back():
  timmy.backward(10)
  timmy.color("green")
  timmy.pensize(8)
  
def turn_left():
  # timmy.left(5)
  timmy.setheading(timmy.heading()-5)
  
def turn_right():
  # timmy.right(5)
  timmy.setheading(timmy.heading()+5)
  
def clear_screen():
  timmy.clear()
  timmy.penup()
  timmy.home()
  timmy.pd()
  
  
# screen.onkey(key="a",fun=forward)
# screen.onkey(key="w",fun=back)
# screen.onkey(key="Up",fun=turn_right)
# screen.onkey(key="Down",fun=turn_left)
# screen.onkey(key="c",fun=clear_screen)

screen.onkey(forward,"a")
screen.onkey(back,"w")
screen.onkey(turn_right,"Up")
screen.onkey(turn_left,"Down")
screen.onkey(clear_screen,"c")

screen.exitonclick()