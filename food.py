import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.shapesize(0.5, 0.5)
        self.color("Chartreuse4")
        self.speed(10)

    def refresh(self):
        rand_x = random.randrange(-280, 281)
        rand_y = random.randrange(-280, 281)
        self.goto(rand_x, rand_y)
