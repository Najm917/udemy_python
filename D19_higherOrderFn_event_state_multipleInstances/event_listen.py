from turtle import Turtle,Screen
timmy=Turtle()
Screen=Screen()

def move():
  timmy.forward(10)
def right():
  timmy.right(90)





Screen.listen()
Screen.onkey(key="a" ,fun=move)
Screen.onkey(key="space",fun=right)
Screen.exitonclick()
