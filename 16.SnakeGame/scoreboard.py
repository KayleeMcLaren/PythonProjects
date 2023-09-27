from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    # Initializes the scoreboard object
    def __init__(self):
        super().__init__()
        self.score = 0  # sets the score to 0
        self.color("white")  # sets the color to white
        self.penup()  # turns off the pen
        self.goto(0, 270)  # moves the scoreboard to the top center of the game window
        self.hideturtle()  # hides the scoreboard
        self.update_scoreboard()  # calls the update_scoreboard() method

    #  Writes the current score to the scoreboard
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    # Writes the "GAME OVER" message to the center of the game window
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    # Increases the score by 1 and updates the scoreboard
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
