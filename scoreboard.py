from turtle import Turtle

FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pendown()
        self.hideturtle()
        self.setpos(0, 270)
        self.color("white")
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def update_score(self):
        self.write(f"Score: {self.score}", False, "center", FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()
