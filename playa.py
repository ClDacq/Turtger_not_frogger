from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
Ocean= 280


class PreciousLilOne(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_right(self):
        self.right(MOVE_DISTANCE)
    def go_left(self):
        self.left(MOVE_DISTANCE)

    def go_down(self):
        self.backward(MOVE_DISTANCE)

    def leap_forward(self):
        self.forward(MOVE_DISTANCE * 3)
    
    def go_to_start(self):
        self.goto(STARTING_POSITION)
        
    def made_it_safe(self):
        if self.ycor() > Ocean:
            return True
        else:
            return False
