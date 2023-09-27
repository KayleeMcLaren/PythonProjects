from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5  # The initial speed of the cars
MOVE_INCREMENT = 10  # The amount by which the car speed increases each level


class CarManager:

    # Initializes the all_cars list and the car_speed variable
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    # Creates a new car and adds it to the all_cars list
    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)  
            new_car.goto(300, random_y)  # The car is created at a random y-coordinate at the top of the screen
            self.all_cars.append(new_car)

    # Moves all of the cars down the screen
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)  #  The cars move backwards because they are facing the top of the screen

    # Increases the speed of the cars by the MOVE_INCREMENT amount
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
