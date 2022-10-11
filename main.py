from turtle import Screen
import time
import snake
from food import Food
from scoreboard import Scoreboard


snake = snake.Snake()
food = Food()
scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
turtle_list = []

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    distance = snake.head.distance(food)
    if distance < 15:
        food.move_food()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        scoreboard.reset()
        snake.reset_snake()


    # Detect collision with tail
    for single in snake.turtle_list[1:]:
        if snake.head.distance(single) < 10:
            scoreboard.reset()
            snake.reset_snake()



screen.exitonclick()
