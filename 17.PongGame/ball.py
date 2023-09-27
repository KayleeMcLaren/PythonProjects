from turtle import Turtle


class Ball(Turtle):

    # __init__() method is the constructor for the Ball class. It is called when a new Ball object is created
    def __init__(self):
        super().__init__()  # super().__init__() call initializes the Ball object as a Turtle object
        # Sets the initial properties of the Ball object
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1


    # Moves the ball by adding its x- and y-velocity to its current x- and y-coordinates
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1   # Reverses the ball's y-velocity, causing it to bounce off of a wall or paddle
 
    def bounce_x(self):
        self.x_move *= -1  # Reverses the ball's x-velocity, causing it to bounce off of a wall or paddle.
        self.move_speed *= 0.9  # Reduces the ball's movement speed by 10%, to simulate friction

    
    def reset_position(self):
        self.goto(0, 0)  # Moves the ball back to the center of the screen
        self.move_speed = 0.1  # Sets its movement speed to its initial value
        self.bounce_x()  # Reverses the ball's x-velocity, to ensure that it is moving away from the paddle that hit it
