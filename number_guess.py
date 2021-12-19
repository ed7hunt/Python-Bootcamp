import random
# http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
from number_guess_art import logo

# globals
max_number = 100
magic_number = random.randint(1, max_number)


def get_number_of_guesses(level):
    if level == "easy":
        return 10
    else:
        return 5


def check_if_magic_number(new_guess, n1):
    if new_guess == magic_number:
        return f"YOU GUESSED IT! The number was {magic_number}."
    if new_guess > magic_number:
        return f"The magic number is LOWER than your guess. Only {n1} left."
    if new_guess < magic_number:
        return f"The magic number is HIGHER than your guess. Only {n1} left."


def main():
    print(f"Welcome to{logo}")
    lev = str(input("Choose a level. easy or hard?: "))
    guesses = get_number_of_guesses(lev)
    out_of_guesses = False
    your_guess = int()
    print(f"You have {guesses} guesses total. The number is between 1 and {max_number}.")
    while (not out_of_guesses) and your_guess != magic_number:
        your_guess = int(input("Choose a number: "))
        guesses -= 1
        result = check_if_magic_number(your_guess, guesses)
        print(result)
        if guesses <= 0:
            out_of_guesses = True
            print(f"You ran out of guesses. You LOSE. The number was {magic_number}.")


main()
