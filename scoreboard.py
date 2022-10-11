from turtle import Turtle

FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt", mode='r') as file:
            contents = file.read()
            if contents != "":
                self.high_score = int(contents)
            else:
                self.high_score = 0


        self.penup()
        self.hideturtle()
        self.setpos(-75, 270)
        self.color("white")
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.clear()
        self.update_score()

    def update_score(self):
        self.goto(0, 270)
        self.write(f"Score: {self.score} High score: {self.high_score}", False, "center", FONT)

    def save_high_score(self):
        with open("high_score.txt", mode='w') as file:
            file.write(str(self.high_score))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()
