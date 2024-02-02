from turtle import Turtle
import random as rd
COLORS = ["medium orchid", "pale violet red", "purple", "indian red"]
y_list = range(-210,210,30)
class CarManager:
    def __init__(self):
        self.new_car = []
        self.speed = 10
    def make_car(self):
        chance = rd.randint(1,8)
        rd_color = rd.choice(COLORS)
        rd_y = rd.choice(y_list)
        starting_x = 280
        if chance == 1:
            body = Turtle()
            body.shape("square")
            body.shapesize(stretch_len=2, stretch_wid=1)
            body.color(rd_color)
            body.penup()
            body.goto(starting_x, rd_y)
            self.new_car.append(body)
            tire1 = Turtle()
            tire1.shape("circle")
            tire1.color(rd_color)
            tire1.penup()
            tire1.goto(starting_x-15, rd_y-10)
            self.new_car.append(tire1)
            tire2 = Turtle()
            tire2.shape("circle")
            tire2.color(rd_color)
            tire2.penup()
            tire2.goto(starting_x + 15, rd_y - 10)
            self.new_car.append(tire2)
    def move_car(self):
        for seg in self.new_car:
            seg.backward(self.speed)
    def sped_up(self):
        self.speed += 5