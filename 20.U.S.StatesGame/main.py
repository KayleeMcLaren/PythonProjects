import turtle
import pandas

# Creates a new turtle screen and sets its title to "U.S. States Game"
screen = turtle.Screen()
screen.title("U.S. States Game")
# Adds the image blank_states_img.gif to the screen and sets the turtle's shape to the image
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Reads the CSV file 50_states.csv into a Pandas DataFrame and assigns it to the variable data
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()  # Extracts the list of states from the DataFrame and assigns it to the variable all_states
guessed_states = []  #  Initializes an empty list to store the guessed states and assigns it to the variable guessed_states

# Starts a while loop that will continue until the player has guessed all 50 states
while len(guessed_states) < 50:
    # Prompts the player to enter the name of a state
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",  # Displays the number of states that the player has guessed so far
                                    prompt="What's another state's name?").title()
    # If the player enters "Exit", the loop is broken and the program ends
    if answer_state == "Exit":
        missing_states = []  # Creates a list of the states that the player has not guessed yet and assigns it to the variable missing_states
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)  # Creates a new Pandas DataFrame from the list of missing states and assigns it to the variable new_data
        new_data.to_csv("states_to_learn.csv")  # Writes the DataFrame to a CSV file called states_to_learn.csv
        break
    # If the player enters a valid state name, the code proceeds into this block
    if answer_state in all_states:
        guessed_states.append(answer_state)  # Appends the guessed state to the guessed_states list
        t = turtle.Turtle()  # Creates a new turtle to write the state name on the map
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))  # The turtle's position is set to the coordinates of the state in the DataFrame
        t.write(answer_state)  # The state name is written on the map
