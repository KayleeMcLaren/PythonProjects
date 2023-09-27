from turtle import Turtle
import random


class Food(Turtle):

    # Initializes the food object
    def __init__(self):
        super().__init__()  # super().__init__() in the Food class is a call to the __init__() method of the parent class, which in this case is the Turtle class
        self.shape("circle")  # sets the shape to a circle
        self.penup()  # turns off the pen
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # sets the size to half the size of a regular turtle
        self.color("blue")  # sets the color to blue
        self.speed("fastest")  # sets the speed to the fastest speed
        self.refresh()  # calls the refresh() method

    # Moves the food to a random location within the game window
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
