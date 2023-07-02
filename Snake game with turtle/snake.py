from turtle import Turtle

POS = [(0, 0), (-20,0), (-40, 0)]
M_D = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()


    def create_snake(self):
        for i in POS:
            self.add_element(i)

    def add_element(self,posi):
        t1 = Turtle("square")
        t1.penup()
        t1.color("white")
        t1.goto(posi)
        self.segments.append(t1)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()

    def extend(self):
        self.add_element(self.segments[-1].position())

    def move(self):
        for sn in range(len(self.segments)-1,0,-1):
            n_x = self.segments[sn - 1].xcor()
            n_y = self.segments[sn - 1].ycor()
            self.segments[sn].goto(n_x, n_y)
        self.segments[0].forward(M_D)

    def up(self):
        if self.segments[0].heading() == 270:
            pass
        else:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() == 90:
            pass
        else:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() == 0:
            pass
        else:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() == 180:
            pass
        else:
            self.segments[0].setheading(0)
