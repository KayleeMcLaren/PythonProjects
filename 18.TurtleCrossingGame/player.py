from turtle import Turtle

STARTING_POSITION = (0, -280)  #  The initial position of the player on the screen
MOVE_DISTANCE = 10  #  The distance by which the player moves each time the go_up() method is called
FINISH_LINE_Y = 280  # The y-coordinate of the finish line


class Player(Turtle):

    # Initializes the player's shape, position, and heading
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    # Moves the player forward by the MOVE_DISTANCE amount
    def go_up(self):
        self.forward(MOVE_DISTANCE)

    # Moves the player to the starting position
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    # Checks if the player has reached the finish line
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:  # Chekcs if the player's y-coordinate is greater than the finish line y-coordinate
            return True
        else:
            return False
