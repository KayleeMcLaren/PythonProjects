from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    # Initializes the scoreboard object
    def __init__(self):
        super().__init__()
        self.score = 0  # sets the score to 0
        with open("data.txt") as data:  # used to read the high score from a file - "data.txt"
            self.high_score = int(data.read())
        self.color("white")  # sets the color to white
        self.penup()  # turns off the pen
        self.goto(0, 270)  # moves the scoreboard to the top center of the game window
        self.hideturtle()  # hides the scoreboard
        self.update_scoreboard()  # calls the update_scoreboard() method

    #  Clears the screen and writes the current score to the scoreboard
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # Resets the scoreboard to its initial state
     def reset(self):
        # Checks if the current score is greater than the high score
        if self.score > self.high_score:
            self.high_score = self.score
            # If it is, the high score is updated and saved to a file
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        # The score is then reset to 0 and the scoreboard is updated
        self.score = 0
        self.update_scoreboard()

    # Increases the score by 1 and updates the scoreboard
     def increase_score(self):
        self.score += 1
        self.update_scoreboard()
