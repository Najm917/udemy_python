# this method is create a list/tupple of a color


# import colorgram
# colors = colorgram.extract(r'd:\udemy revise\D18_Turtle_GUI\random_art\OIP.jpg', 30)

# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

# __________________________________
from turtle import Turtle, Screen
import random

# Background jaise halkay colors hata diye hain
color_list = [
    (200, 162, 98), (62, 89, 127), (139, 90, 47), (135, 170, 191), 
    (218, 206, 117), (29, 39, 65), (132, 27, 52), (149, 62, 86), 
    (76, 15, 33), (167, 153, 49), (130, 181, 144), (186, 141, 161), 
    (43, 57, 100), (184, 94, 107), (53, 37, 25), (61, 123, 107), 
    (92, 116, 175), (80, 76, 31), (89, 151, 100), (80, 147, 159), 
    (194, 87, 73), (220, 174, 186), (166, 207, 161), (163, 201, 215), 
    (31, 55, 52), (145, 35, 22)
]

yimmy = Turtle()
yimmy.penup()
yimmy.hideturtle()
yimmy.speed("fastest")

screen = Screen()
screen.colormode(255)

yimmy.setheading(225)
yimmy.forward(300)
yimmy.setheading(0)

for dot_count in range(1, 101):
    yimmy.dot(20, random.choice(color_list))
    yimmy.forward(50)

    if dot_count % 10 == 0:
        yimmy.setheading(90)  
        yimmy.forward(50)     
        yimmy.setheading(180)  
        yimmy.forward(500)     
        yimmy.setheading(0)   

screen.exitonclick()