from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    # Initializes the snake object
    def __init__(self):
        self.segments = []  # creates an empty list to store the snake segments
        self.create_snake()  # calls the create_snake() method to create the initial segments
        self.head = self.segments[0]  # sets the head of the snake to the first segment

    # Creates a new snake segment for each position in the STARTING_POSITIONS list - 3 starting segments
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)  

    # Adds a new segment to the tail of the snake
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)  

    #  Calls the add_segment() method to extend the snake by one segment
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # Moves the snake forward by one segment
    def move(self):
        # It does this by iterating over the segments list in reverse order, starting with the last segment
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)  # For each segment, it moves the segment to the current position of the previous segment
        self.head.forward(MOVE_DISTANCE)  # The head of the snake is then moved forward by the MOVE_DISTANCE

    # The up(), down(), left(), and right() methods set the heading of the snake's head in the specified direction. 
    # However, they only do this if the snake's head is not currently heading in the opposite direction
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
