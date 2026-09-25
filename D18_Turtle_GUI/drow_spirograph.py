import random
from turtle import Turtle,Screen

# heading() returns the turtle's current orientation as an angle between 0 and 360 degrees.

# setheading() sets the turtle's orientation to an absolute compass angle, regardless of where it was pointing before.

timmy=Turtle()
Screen=Screen()
Screen.colormode(255)

def random_color():
  r=random.randint(0,255)
  g=random.randint(0,255)
  b=random.randint(0,255)
  return (r,g,b)
def set_angle(angle):
    
  for _ in range(int(360/angle)):
    timmy.speed("fastest")
    timmy.color(random_color())
    timmy.circle(75)
    timmy.setheading(timmy.heading()+angle)

set_angle(36)



















Screen.exitonclick()