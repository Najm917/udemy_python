import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
car_manager=CarManager()
score=Scoreboard()
screen.listen()
screen.onkey(player.move_turtle_up,"Up")
screen.onkey(player.move_turtle_down,"Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    car_manager.create_car()
    car_manager.move__car()
    
    
    
# detect car with turtle
    for car in car_manager.all_cars:
        if car.distance(player)<20:
            game_is_on=False
            score.game_over()
            
    if player.is_finish_line():
        player.go_to_staring()
        car_manager.level_up()
        score.increase_level()
screen.exitonclick()