from  turtle import Turtle,Screen
import random
is_race_on=False
screen=Screen()
# width=x height=y
screen.setup(width=1000, height=600)
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color (red, orange, yellow, green, blue, purple): "
)
screen.bgcolor("gray")
colors=["red","green","black","yellow","blue","white","purple"]
y_positions = [-180, -120,-60,0, 60, 120, 180]

all_turtles = []
for turtle_index in range(7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-450, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)
if user_bet:
  is_race_on=True
  
while is_race_on:
  for turtle in all_turtles:
    if turtle.xcor() > 460:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color.lower() == user_bet.lower():
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost! The {winning_color} turtle won the race!")
            break
    rand_distance=random.randint(0,10)
    turtle.forward(rand_distance)
    
    
screen.exitonclick()