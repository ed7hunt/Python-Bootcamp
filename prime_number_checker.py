def prime_checker(number):
    prime = False
    for count in range(2, number):
        remainder = number % count
        if remainder == 0:
            print(f"{number} is divisible by {count}")
            prime = True
    if prime:
        print(f"{number} is not a prime number.")
    else:
        print(f"{number} is a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)
