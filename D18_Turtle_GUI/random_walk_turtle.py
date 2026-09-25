from turtle import Turtle,Screen
import random
screen=Screen()
screen.colormode(255)
timmy=Turtle()

# colors=(
#   "aquamarine", "chartreuse", "coral", "cornflowerblue",
#     "darkorchid", "deepskyblue", "firebrick", "gold",
#     "hotpink", "lawngreen", "maroon", "mediumspringgreen",
#     "orangered", "peru", "royalblue", "sienna", "tomato"
# )
def random_color():
  r=random.randint(0,255)
  g=random.randint(0,255)
  b=random.randint(0,255)
  
  return (r,g,b)

direction=[0,90,180,270]



timmy.pensize(10)
timmy.speed("fast")

for _ in range(200):
  timmy.shape("turtle")
  timmy.color(random_color())
  timmy.forward(30)
  timmy.setheading(random.choice(direction))







screen.exitonclick()