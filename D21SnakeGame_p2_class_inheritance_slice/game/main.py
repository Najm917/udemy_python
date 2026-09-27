from turtle import Screen
import time
from body import Snake
from food import Foood
from score import Score

# _______________________________________
screen=Screen()
screen.listen()
screen.title("Snake Game ")
screen.setup(width=600,height=600)
screen.bgcolor("#614E4E")
screen.tracer(0)

# _______________________________________
# body
snake=Snake()
food=Foood()
score=Score()

# _________________________________
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
  
    
  if snake.head.distance(food)<15:
    
    food.refresh()
    snake.increase_body()
    score.update_scoreboard()
    score.increase_score()
    
    
  
  
    
  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
    score.game_over()
    is_game_on = False
    
  for segment in snake.segments:
    if segment==snake.head:
      pass
    elif snake.head.distance(segment)<10:
      is_game_on=False
      score.game_over()
    
# __________________________________
# moving




screen.exitonclick()