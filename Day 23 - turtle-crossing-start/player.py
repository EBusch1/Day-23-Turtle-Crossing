from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("turtle")
        self.setheading(90)
        self.starting_position()

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def move_backward(self):
        self.forward(MOVE_DISTANCE * -1)

    def starting_position(self):
        self.goto(STARTING_POSITION)
