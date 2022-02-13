FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("Black")
        self.hideturtle()
        self.penup()

    def display_score(self):
        self.clear()
        self.goto(-250, 250)
        self.write(f"Score: {self.score}", font=FONT)



    def you_lose(self):
        self.goto(0, 0)
        self.write(f"You lose!!", font=FONT)
