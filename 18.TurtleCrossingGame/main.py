import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Creates a new turtle.Screen object and sets its properties
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Creates instances of the Player, CarManager, and Scoreboard classes
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Tells the turtle screen to listen for keyboard events. When the Up arrow key is pressed, the player.go_up() method is called
screen.listen()
screen.onkey(player.go_up, "Up")

# The game loop will continue running until the game_is_on variable is set to False
game_is_on = True
while game_is_on:
    # Waits for 0.1 seconds before updating the screen
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()  # Creates a new car at the top of the screen
    car_manager.move_cars()  # Moves all of the cars down the screen

    # Checks if the player has collided with any of the cars. 
    for car in car_manager.all_cars:
        if car.distance(player) < 20:  # Checks if the distance between the player and the car is less than 20 pixels
            # If so, the game is over and the scoreboard.game_over() method is called
            game_is_on = False
            scoreboard.game_over()

    # Checks if the player has reached the finish line. 
    if player.is_at_finish_line():
        # If so, the player is moved to the start of the road, the cars are made to move faster, and the player's score is increased
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()
