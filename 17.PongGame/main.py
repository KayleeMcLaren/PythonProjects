from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Creates a new turtle.Screen object and sets its properties
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)  # Disables the turtle screen's automatic update

# Creates instances of the Paddle, Ball, and Scoreboard classes
r_paddle = Paddle((350, 0))  # Placed at the right of the screen
l_paddle = Paddle((-350, 0))  # Placed at the left of the screen
ball = Ball()  # The Ball instance is placed in the center of the screen
scoreboard = Scoreboard()

screen.listen()  # Listens for keyboard events
# When the Up or Down arrow keys are pressed, the corresponding Paddle object is moved up or down
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
# When the w or s keys are pressed, the corresponding Paddle object is moved up or down
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Main game loop - continue running until the game_is_on variable is set to False
game_is_on = True
while game_is_on:
    # Waits for 0.1 seconds before updating the screen and moving the ball. This slows down the game loop and makes it more playable
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Checks if the ball has hit the top or bottom wall. If so, the ball's y-velocity is reversed
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Checks if the ball has hit the right or left paddle. If so, the ball's x-velocity is reversed
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Checks if the ball has passed the right paddle. If so, the ball is reset to its starting position and the left player scores a point
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Checks if the ball has passed the left paddle. If so, the ball is reset to its starting position and the right player scores a point
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

# Waits for the user to click the screen before closing the game
screen.exitonclick()
