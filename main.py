import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

def get_mouse_click_coor(x, y):
    print(x, y)
states = pandas.read_csv("50_states.csv")
all_states = states.state.to_list()

score = 0
correct_guesses = []
game_on = True
while game_on:
    if len(correct_guesses) == 50:
        print("You guessed all!")
        game_on = False
    answer_state = screen.textinput(title=f"{score}/50", prompt="Guess a state's name")
    big_first_letter = answer_state.title()
    if big_first_letter == "Exit":
        missing_states = []
        for i in all_states:
            if i not in correct_guesses:
                missing_states.append(i)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if big_first_letter in correct_guesses:
        print("You guessed that already")
        continue
    if big_first_letter in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(states._get_value(all_states.index(big_first_letter), "x"), states._get_value(all_states.index(big_first_letter), "y"))
        t.write(big_first_letter, move=False, font=("Verdana", 8, "normal"))
        score += 1
        correct_guesses.append(big_first_letter)
        print(correct_guesses)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()