# Remember to use the random module
# Hint: Remember to import the random module first. 🎲

import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
# 🚨 Don't change the code above 👆 It's only for testing your code.

# Write your code below this line 👇

output_list = ["Tails", "Heads"]
flip = random.randint(0, 1)
print(output_list[flip])
