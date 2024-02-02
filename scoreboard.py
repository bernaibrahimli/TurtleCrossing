from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-280,-280)
        self.hideturtle()
        self.level = 1
        self.color("white")
        self.write(f"Level: {self.level}", font=('Arial', 20, 'normal'))
    def update_sb(self, level):
        self.clear()
        self.color("white")
        self.write(f"Level: {level}", font=('Arial', 20, 'normal'))
    def game_over(self):
        game_over = Turtle()
        game_over.penup()
        game_over.hideturtle()
        game_over.goto(-60,0)
        game_over.color("white")
        game_over.write("Game Over", font=('Arial', 30, 'normal'))
