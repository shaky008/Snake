from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 225)
        self.write(f"score: {self.score}", False, "center", font=("Arial", 15, "normal"))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"score: {self.score}", False, "center", font=("Arial", 15, "normal"))

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", font=("Arial", 15, "normal"))
