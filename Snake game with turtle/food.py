from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.6,0.6)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        self.goto(x, y)
