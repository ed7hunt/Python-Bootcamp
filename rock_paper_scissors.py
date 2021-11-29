import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
outcome = [rock, paper, scissors]
choice_string = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
choice = int(choice_string)
computer_choice = random.randint(0, 2)
# choice rock = 0
if choice == 0:
    # scissors
    if computer_choice == 2:
        print(f"{outcome[0]}\n {outcome[2]}\nYou win!")
    # rock
    elif computer_choice == 0:
        print(f"{outcome[0]}\n {outcome[0]}\nDraw")
    # paper
    else:
        print(f"{outcome[0]}\n {outcome[1]}\nYou lose!")
# choice paper
elif choice == 1:
    # scissors
    if computer_choice == 2:
        print(f"{outcome[1]}\n {outcome[2]}\nYou lose!")
    # rock
    elif computer_choice == 0:
        print(f"{outcome[1]}\n {outcome[0]}\nYou win!")
    # paper
    else:
        print(f"{outcome[1]}\n {outcome[1]}\nDraw")
# choice scissors
elif choice == 2:
    # scissors
    if computer_choice == 2:
        print(f"{outcome[2]}\n {outcome[2]}\nDraw")
    # rock
    elif computer_choice == 0:
        print(f"{outcome[2]}\n {outcome[0]}\nYou Lose!")
    # paper
    else:
        print(f"{outcome[2]}\n {outcome[1]}\nYou win!")
else:
    print("You picked an invalid number. You Lose!")
    
