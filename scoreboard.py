from turtle import Turtle

FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score =0
        self.penup()
        self.hideturtle()
        self.setpos(-75, 270)
        self.color("white")
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.clear()
        self.update_score()

    def update_score(self):
        self.goto(0, 270)
        self.write(f"Score: {self.score} High score: {self.high_score}", False, "center", FONT)


    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()




