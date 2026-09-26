from turtle import Turtle,Screen
import random,time
from body import Snake
# _______________________________________
screen=Screen()
screen.listen()
screen.title("Snake Game ")
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)

# _______________________________________
# body
snake=Snake()
screen.onkey(snake.move_up,"Up")
screen.onkey(snake.move_down,"Down")
screen.onkey(snake.move_left,"Left")
screen.onkey(snake.move_right,"Right")
# _________________________________
is_game_on=True
while is_game_on:
  screen.update()
  time.sleep(.1)
  snake.move()
  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    is_game_on = False

  
    
# __________________________________
# moving




screen.exitonclick()