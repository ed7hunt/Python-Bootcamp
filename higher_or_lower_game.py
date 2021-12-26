import random
from higher_lower_art import logo
from higher_lower_art import vs
from higher_lower_game_data import data
from replit import clear

# globals
data_count = len(data) - 1


def pick_new_category():
    pick_new_random_category = data[random.randint(0, data_count)]
    return pick_new_random_category


def game_begin():
    your_score = 0
    print(logo)
    older = pick_new_category()
    while True:
        guess = ""
        if your_score >= 1:
            clear()
            print(logo)
            print(f"You're Right! Current score = {your_score} ")
        print(f"Compare A: {older['name']}, a {older['description']}, from {older['country']}")
        print(vs)
        newer = pick_new_category()
        print(f"Against B: {newer['name']}, a {newer['description']}, from {newer['country']}")
        while guess == "":
            guess = str(input(f"Which has more followers [A,B]?  "))
            if guess != "A" and guess != "B":
                print("Invalid guess. Try again.")
                guess = ""
        if guess == "A":
            if older['follower_count'] >= newer['follower_count']:
                # you win
                your_score += 1
                older = newer
            else:
                return your_score
        elif guess == "B":
            if older['follower_count'] <= newer['follower_count']:
                # you win
                your_score += 1
                older = newer
            else:
                return your_score


final_score = game_begin()
print(f"Game over. You scored {final_score}.")
if final_score <= 3:
    print("You are horrible!")
elif final_score <= 8:
    print("You didn't do too shabby.")
else:
    print("You scored in the top 10%")
