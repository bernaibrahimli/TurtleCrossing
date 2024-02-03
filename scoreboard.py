from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-280,-280)
        self.hideturtle()
        self.score = 0
        with open("high_score.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
    def update_sb(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.clear()
        self.color("white")
        self.write(f"Score: {self.score}  High Score: {self.high_score}", font=('Arial', 20, 'normal'))
    def game_over(self):
        game_over = Turtle()
        game_over.penup()
        game_over.hideturtle()
        game_over.goto(-60,0)
        game_over.color("white")
        game_over.write("Game Over", font=('Arial', 30, 'normal'))
