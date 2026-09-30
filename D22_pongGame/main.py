from turtle import Screen
from paadle import Paddle
from ball import Ball
from scor import ScoreBord
import time

screen=Screen()
screen.listen()
screen.title("pong")
screen.bgcolor("#000000")
screen.setup(800,600)
screen.tracer(0)

r_paddle=Paddle((360,0))
l_paddle=Paddle((-360,0))
ball=Ball()
score=ScoreBord()



  
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"a")
screen.onkey(l_paddle.go_down,"w")

is_gameon=True
while is_gameon:
  time.sleep(ball.move_speed)
  screen.update()
  ball.random_move()
  
# detect ball with ycor() and bounce
  if ball.ycor()>280 or ball.ycor()<-280:
    ball.boune_ball_y()
    
    
# detect ball with xcor and paddle them bounce
  if ball.distance(r_paddle)<50 and ball.xcor()>330 or ball.distance(l_paddle)<50 and ball.xcor()<-330:
    ball.boune_x_paddle()
  
  
  if ball.xcor()>380 :
    
    ball.miss_ball()
    score.l_points() 
    
  if ball.xcor()<-380:
    ball.miss_ball()
    score.r_points()
    
screen.exitonclick()