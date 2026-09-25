from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()
screen.colormode(255)

def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# for _ in range(3):
#   timmy.color(get_random_color())
#   timmy.forward(90)
#   timmy.right(120)
  
# for _ in range(4):
#     timmy.color(get_random_color())
#     timmy.forward(90)
#     timmy.right(90)

# for _ in range(5):
#   timmy.color(get_random_color())
#   timmy.forward(90)
#   timmy.right(72)
  
# for _ in range(6):
#   timmy.color(get_random_color())
#   timmy.forward(90)
#   timmy.right(60)
  
# for _ in range(7):
#   timmy.color(get_random_color())
#   timmy.forward(90)
#   timmy.right(51.54)
  
# for _ in range(8):
#   timmy.color(get_random_color())
#   timmy.forward(90)
#   timmy.right(45)
  
  
# _____________________________________
for sides in range(3, 11):
    timmy.color(get_random_color())  
    angle = 360 / sides              # Exact turn angle for any regular polygon
    for _ in range(sides):
        timmy.forward(90)
        timmy.right(angle)
        
# ____________________________________
# def draw_shape(num_side):
#   angle=360/num_side
#   for _ in range(num_side):
#     timmy.forward(100)
#     timmy.right(angle)
    
# for shape_side in range(3,11):
#   draw_shape(shape_side)
#   timmy.color(get_random_color())
  
screen.exitonclick()