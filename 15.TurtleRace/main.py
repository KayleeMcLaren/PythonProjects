from turtle import Turtle, Screen
import random

# These lines set up the race
is_race_on = False  # Tracks whether the race is still in progress
screen = Screen()  # Create a new turtle graphics window
screen.setup(width=500, height=400)  # Sets the size of the window
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")  # Stores the user's bet on which turtle will win the race
colors = ["red", "orange", "yellow", "green", "blue", "purple"]  # Contains the colors of the turtles
y_positions = [-70, -40, -10, 20, 50, 80]  # Contains the y-positions of the turtles at the start of the race
all_turtles = []  # Stores all the turtles in the race

# Creates 6 turtles, one for each color in the colors list
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])  # The turtles are given the appropriate colour
    new_turtle.goto(x=-230, y=y_positions[turtle_index])  # Each turtle is positioned at the start of the race, with a y-position that corresponds to its index in the y_positions list
    all_turtles.append(new_turtle)

# Checks if the user has placed a bet. If so, the is_race_on variable is set to True and the race begins
if user_bet:
    is_race_on = True

# This loop simulates the race
while is_race_on:
    for turtle in all_turtles:
        # 230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:  # The race ends when one of the turtles crosses the finish line (i.e., when its x-coordinate is greater than 230)
            is_race_on = False
            winning_color = turtle.pencolor()  # The winning turtle's color is then compared to the user's bet
            # If the colors match, the user wins. Otherwise, the user loses
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        # Makes each turtle move a random amount
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# Tells the turtle graphics window to remain open until the user clicks on it
screen.exitonclick()
