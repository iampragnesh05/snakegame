from multiprocessing.pool import worker
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("data.txt") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            self.high_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def game_over(self):
        self.reset()
        self.goto(0,0)
        self.write(f"Game over", align="center", font=("Courier", 24, "normal"))