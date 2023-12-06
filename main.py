import turtle
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Drake")
screen.tracer(0)

food = Food()
snake = Snake()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        score.score_updater()
    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290:
        scoreboard.reset()


    # Detect Collision with tail
    for segment in snake.snake_list[1:-1]:
        if snake.head.distance(segment) < 10:
            game_is_on = False

screen.exitonclick()
