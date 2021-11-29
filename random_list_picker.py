import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

names_length = len(names)
lucky_name = names[random.randint(0, names_length - 1)]
print(f"{lucky_name} is going to buy the meal today!")
