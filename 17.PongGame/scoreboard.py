from turtle import Turtle


class Scoreboard(Turtle):

    # __init__() method is the constructor for the Scoreboard class. It is called when a new Scoreboard object is created
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0  # Initializes the left player's score to 0
        self.r_score = 0  # Initializes the right player's score to 0
        self.update_scoreboard()  #  Updates the scoreboard to display the current scores

    #  Clears the scoreboard and then writes the current scores to the screen, using the write() method
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    # Increments the left player's score by 1 and then updates the scoreboard
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    # Increments the right player's score by 1 and then updates the scoreboard
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
