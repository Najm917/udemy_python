from turtle import Turtle,Screen
Screen=Screen()
Screen.title("Racing game")
Screen.bgcolor("gray")
Screen.listen()
Screen=Screen.setup(width=1000, height=600)
# user_bet=Screen.textinput(title="make your bet",prompt="which turtle will win the race? enter a color: ")

timmy=Turtle("turtle")
timmy.color("red")
timmy.penup()
timmy.goto(x=-450, y=-150)
  
tomy=Turtle("turtle")
tomy.color("red")
tomy.penup()
tomy.goto(x=-450, y=-90)

jrary=Turtle("turtle")
jrary.color("red")
jrary.penup()
jrary.goto(x=-450, y=-30)

jony=Turtle("turtle")
jony.color("red")
jony.penup()
jony.goto(x=-450, y=30)

jack=Turtle("turtle",)
jack.color("red")
jack.penup()
jack.goto(x=-450, y=90)

jamy=Turtle("turtle")
jamy.color("red")
jamy.penup()
jamy.goto(x=-450, y=150)

# Screen.color("red")
Screen.exitonclick()
