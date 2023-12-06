from turtle import Turtle

S_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIS = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]

    def create_snake(self):
        for seat in S_POSITIONS:
            self.add_snake_segment(seat)

    def add_snake_segment(self, seat):
        # add a new segment to the snake
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.speed("fastest")
        new_snake.up()
        new_snake.goto(seat)
        self.snake_list.append(new_snake)

    def extend_snake(self):
        self.add_snake_segment(self.snake_list[-1].pos())

    def move(self):
        for s in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[s - 1].xcor()
            new_y = self.snake_list[s - 1].ycor()
            self.snake_list[s].goto(new_x, new_y)
        self.snake_list[0].forward(MOVE_DIS)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
