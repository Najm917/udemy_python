from turtle import Screen
import time
from body import Snake
from food import Foood,SpecialFood
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
special_food=SpecialFood()
score=Score()

# _________________________________
screen.onkey(snake.move_up,"Up")
screen.onkey(snake.move_down,"Down")
screen.onkey(snake.move_left,"Left")
screen.onkey(snake.move_right,"Right")
# _________________________________
is_game_on=True
food_counter=0

while is_game_on:
  screen.update()
  time.sleep(.1)
  snake.move()
  
    
  if snake.head.distance(food)<15:
    
    food.refresh()
    snake.increase_body()
    score.update_scoreboard()
    score.increase_score()
    food_counter+=1
  
# detect how much food ead every 5 ead show special food
    if food_counter==5:
      special_food.spawn()
      food_counter=0
    
# special food time count down
  if special_food.is_active:
    if time.time()-special_food.spawn_time>10:
      special_food.disappear()
# special food bonus point add
  if special_food.is_active and snake.head.distance(special_food) < 20:
        score.increase_score(points=10)
        snake.increase_body()
        special_food.disappear()
  
    
  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
    score.game_over()
    is_game_on = False
    
  for segment in snake.segments[1:]:
    
    if snake.head.distance(segment)<10:
      is_game_on=False
      score.game_over()
    
# __________________________________
# moving




screen.exitonclick()