import pandas as pd
from turtle import Screen, Turtle

states_df = pd.read_csv("50_states.csv")
states_df["state"] = states_df["state"]

FONT = ("Arial", 10, "bold")

text = Turtle()
text.penup()
text.hideturtle()

screen = Screen()
screen.setup(725, 491)
screen.bgpic("blank_states_img.gif")
screen.title("Name the States")

game_is_on = True
correct_guesses = 0
guessed_states = []
list_all_states = list(states_df["state"])

while correct_guesses != 50:
    guess = screen.textinput(title=f"{correct_guesses}/50 States Correct",
                             prompt="What's another state name?").title()

    if guess == "Exit":
        for state in guessed_states:
            if state in list_all_states:
                list_all_states.remove(state)
        df = pd.DataFrame(list_all_states, columns=["States To Learn"])
        df.to_csv('states_to_learn.csv')
        break

    if guess in list_all_states:
        guessed_states.append(guess)
        row = states_df[states_df["state"] == guess]
        text.goto(int(row["x"]), int(row["y"]))
        text.write(guess, align="center", font=FONT)
        correct_guesses += 1

screen.exitonclick()
