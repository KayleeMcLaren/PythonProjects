from turtle import Turtle

FONT = ("Courier", 24, "normal")  # Defines a constant for the font that will be used for the scoreboard


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1  # Scoreboard's level
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)  # Moves the turtle to the top left corner of the screen
        self.update_scoreboard()

    # Clears the scoreboard and then writes the current level to the screen
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    # Increments the level by 1 and then calls the update_scoreboard() method to update the scoreboard
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    # Moves the scoreboard to the center of the screen and then writes the text "GAME OVER" to the screen, using the specified font
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
