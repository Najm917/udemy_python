from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.turtlesize()
        self.go_to_staring()
        self.setheading(90)
        
    def go_to_staring(self):
        self.goto(STARTING_POSITION)
        
    
    def is_finish_line(self):
        if self.ycor()> FINISH_LINE_Y:
            return True
        else:
            return False
        
    def move_turtle_up(self):
        self.forward(MOVE_DISTANCE)
    def move_turtle_down(self):
        self.backward(MOVE_DISTANCE)
    
