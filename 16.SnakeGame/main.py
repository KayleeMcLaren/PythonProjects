from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Creates a new Screen object and set its properties - width and height of the game window, the background colour, the title of the game window, and the tracer() method sets the speed of the animation
screen = Screen()  
screen.setup(width=600, height=600)  
screen.bgcolor("black")   
screen.title("My Snake Game")  
screen.tracer(0)  # In this case, the tracer is set to 0, which means that the animation will only be updated the screen.update() method is explicitly called 

# Creates new instances of the Snake, Food, and Scoreboard classes
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Tells the screen to listen for keyboard events and to call the corresponding methods on the snake object when the corresponding key is pressed
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop - updates the screen, waits for 0.1 seconds, and then moves the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detects collision with food - if the snake's head is within 15 pixels of the food, the food is refreshed, the snake is extended, and the score is increased
    if snake.head.distance(food) < 15:   
        food.refresh()  
        snake.extend()  
        scoreboard.increase_score()  

    #Detects collision with wall -  if it has, the game is over and the scoreboard's game_over() method is called
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detects collision with it's own tail - if it has, the game is over and the scoreboard's game_over() method is called
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


#  tells the screen to wait for the user to click before closing the game window
screen.exitonclick()
