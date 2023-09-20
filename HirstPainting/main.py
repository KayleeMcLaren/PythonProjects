import turtle as turtle_module
import random

# These lines set up the turtle environment
turtle_module.colormode(255)  # Sets the color mode to 255, which allows the turtle to use any color from a palette of 256 colors
tim = turtle_module.Turtle()  # Turtle() function creates a new turtle object
tim.speed("fastest")  # speed() function sets the turtle's speed to the fastest setting
tim.penup()  # penup() function lifts the turtle's pen so that it does not draw as it moves
tim.hideturtle()  # hideturtle() function hides the turtle so that only the dots it draws are visible

# Creates a list of colors that will be used to draw the dots.
# The list contains 25 colors, each of which is a tuple of three integers representing the red, green,
# and blue components of the color
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

# These lines position the turtle at the top-right corner of the screen and draw a horizontal line to the left
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100  # Sets the number of dots to draw to 100

# This loop draws 100 dots, one at a time
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))  # Each dot is 20 pixels in diameter and is drawn in a random color from the color_list
    tim.forward(50)  # The turtle moves forward 50 pixels after drawing each dot

    # This code block makes the turtle turn 90 degrees to the right every 10 dots
    # This causes the turtle to draw a series of vertical lines, each of which is 50 pixels long
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
