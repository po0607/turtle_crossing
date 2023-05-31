from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.level = 1
        self.penup()
        self.update_score()

    def increase_level(self):
        self.clear()
        self.level += 1
        self.update_score()

    def update_score(self):
        self.goto(x=-280, y=260)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)



