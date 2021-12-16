# Calculator
def addition(n1, n2):
    return n1 + n2


def subtraction(n1, n2):
    return n1 - n2


def multiplication(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}


def calculator():
    num1 = float(input("What is the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Select your function: ")
        num2 = float(input("What is the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(n1=num1, n2=num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if (input(f"Type 'Y' to continue calculation with {answer} or type 'N' to start over? Y/N ")).lower() == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
