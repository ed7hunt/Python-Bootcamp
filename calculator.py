# Calculator
def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x / y


def main():
    print("""
Welcome to Calculator!
+
-
*
/
""")
    z = True
    while z:
        z = False
        function = input("Select your function: ")
        char_one = float(input("What is x? "))
        char_two = float(input("What is y? "))
        if function == "+":
            result = addition(x=char_one, y=char_two)
        elif function == "-":
            result = subtraction(x=char_one, y=char_two)
        elif function == "*":
            result = multiplication(x=char_one, y=char_two)
        elif function == "/":
            result = division(x=char_one, y=char_two)
        else:
            z = True
            print("You entered an invalid function. Try again.")
    print(f"{char_one} {function} {char_two} = {result}")
    answer = input("Would you like to do another? Y/N ")
    if answer.lower() == "y":
        finish = False
    else:
        finish = True
    return finish


finished = False
while not finished:
    finished = main()
