# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lc_name1 = name1.lower()
lc_name2 = name2.lower()
names = lc_name1 + lc_name2
first_digit_count = 0
second_digit_count = 0
first_digit_count += names.count("t")
first_digit_count += names.count("r")
first_digit_count += names.count("u")
first_digit_count += names.count("e")
second_digit_count += names.count("l")
second_digit_count += names.count("o")
second_digit_count += names.count("v")
second_digit_count += names.count("e")
score = int(first_digit_count) * 10
score += int(second_digit_count)
if score < 10 or score > 90:
    print (f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print (f"Your score is {score}, you are alright together.")
else:
    print (f"Your score is {score}.")
    
