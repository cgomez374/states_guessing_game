import turtle
import pandas as pd

# Screen

screen = turtle.Screen()

# Image path

image = 'blank_states_img.gif'

# Add to shapes
screen.addshape(image)
screen.title(f'U.S. States Game')

# Turtle to shape

turtle.shape(image)

# Turtle to write state name

write_turtle = turtle.Turtle()
write_turtle.hideturtle()
write_turtle.penup()
write_turtle.color('black')

# Open the file

data = pd.read_csv('./50_states.csv')

# Place data into lists

states_list = data.state.to_list()
state_x_coord = data.x.to_list()
state_y_coord = data.y.to_list()

# Make strings lowercase

for i in range(len(states_list)):
    states_list[i] = states_list[i].lower()

# Start game

number_of_states = len(states_list)
guessed_correctly = 0
guessed = []

is_game_on = True
while is_game_on:
    # Ask for a state

    answer_state = screen.textinput(title=f"Guess the state {guessed_correctly}/{number_of_states}",
                                    prompt="Whats another state's name?").lower()

    # Check user answer in dictionary

    if answer_state == 'exit':
        is_game_on = False
    elif answer_state in states_list and answer_state not in guessed:
        state_index = states_list.index(answer_state)
        write_turtle.goto(state_x_coord[state_index], state_y_coord[state_index])
        write_turtle.write(arg=f'{answer_state}', move=False, align='center', font=('Arial', 8, 'normal'))
        guessed_correctly += 1
        guessed.append(answer_state)

    if guessed_correctly == number_of_states:
        is_game_on = False

# States not guessed saved to CSV; using list comprehension

not_guessed = [state for state in states_list if state not in guessed]

# Create dict

not_guessed_dict = {
    'states': not_guessed
}

# Create new dataframe

new_csv = pd.DataFrame.from_dict(not_guessed_dict)

# Save as CSV

new_csv.to_csv('states_not_guessed')

# Keeps screen open

turtle.mainloop()
