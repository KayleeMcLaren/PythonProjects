from turtle import Turtle


class Paddle(Turtle):
    
    # __init__() method is the constructor for the Paddle class. It is called when a new Paddle object is created
    def __init__(self, position):  # Position parameter is the initial position of the paddle on the screen
        super().__init__()  # super().__init__() call initializes the Paddle object as a Turtle object
        #  Sets the initial properties of the Paddle object
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    # Moves the paddle up by 20 pixels
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    # Moves the paddle down by 20 pixels
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
