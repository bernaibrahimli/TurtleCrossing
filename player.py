from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(2)
        self.setheading(90)
        self.color("green yellow")
        self.penup()
        self.goto(0,-270)
    def move(self):
        self.forward(10)

    def down(self):
        self.backward(10)

