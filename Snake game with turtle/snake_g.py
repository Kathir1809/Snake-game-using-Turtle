from turtle import Screen, Turtle
tr = Turtle()
import time
from food import Food
from snake import Snake
from score import Score


s = Screen()
s.setup(600,600)
s.bgcolor("black")
s.title("Snake game")
s.tracer(0)

snake = Snake()
food = Food()
sc = Score()

s.listen()

s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")


game = True

while game:
    s.update()
    time.sleep(0.1)
    snake.move()
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        sc.score_refresh()
        snake.extend()

    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
        snake.reset_snake()
        sc.reset_score()
        food.refresh()

    for seg in snake.segments[1:]:
        if snake.segments[0].distance(seg) < 10:
            snake.reset_snake()
            sc.reset_score()
            food.refresh()


s.exitonclick()
