from turtle import Turtle,Screen

timmy=Turtle()

# timmy.shape("turtle")
# timmy.color("red")
# timmy.turtlesize(.5) 
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)


"""______________________________________
              using for loop              
  ________________________________________"""
for _ in range(4):
  timmy.forward(100)
  timmy.right(90)

screen=Screen()
screen.exitonclick()