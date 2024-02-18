from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(f"Score is : {self.score}", align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score >  self.high_score:
            self.high_score = self.score
        self.score = 0
        self.up



    # def game_over(self):
    #     self.penup()
    #     self.goto(0, 0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.clear()
        self.score += 1
        # self.write(f"Score is : {self.score}", align="center", font=("Arial", 20, "normal"))
