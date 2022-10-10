from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtle_list = []
        self.create_snake()
        self.head = self.turtle_list[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_turtle(pos)

    def add_turtle(self, pos):
        t = Turtle("square")
        t.penup()
        t.color("white")
        t.setpos(pos)
        self.turtle_list.append(t)

    def extend(self):
        self.add_turtle(self.turtle_list[-1].position())

    def move(self):
        for turtle_num in range(len(self.turtle_list) - 1, -1, -1):
            if turtle_num != 0:
                new_x = self.turtle_list[turtle_num - 1].xcor()
                new_y = self.turtle_list[turtle_num - 1].ycor()
                self.turtle_list[turtle_num].setpos(new_x, new_y)
            else:
                self.turtle_list[turtle_num].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def get_snake_pos(self):
        return round(self.head.xcor())
