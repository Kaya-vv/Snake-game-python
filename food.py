import turtle
import random
from turtle import Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("darkblue")
        self.speed("fastest")
        self.move_food()

    def get_food_pos(self):
        return round(self.xcor())

    def move_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.setpos(random_x, random_y)