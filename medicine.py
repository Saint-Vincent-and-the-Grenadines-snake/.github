from turtle import Turtle
import random


class MEDICINE(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(1, 0.5)
        self.penup()
        self.color('yellow')
        self.speed('fastest')
        self.penup()
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-260, 280)
        rand_y = random.randint(-260, 280)
        self.goto(rand_x, rand_y)
