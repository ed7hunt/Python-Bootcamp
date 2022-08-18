import random

'''
Example of usage:
    
    from password_generator import generate        # place this line at the top of your Python script to import
    your_password = generate()                     # place this line inside your script to call & store 'your_password'                                         
    
PASSWORD GENERATOR LICENSE
    Copyright (c) 2021, Edward Hunt <ed7hunt@gmail.com>
    PERMISSION TO USE, COPY, MODIFY, AND/OR DISTRIBUTE THIS SOFTWARE FOR ANY PURPOSE WITH OR WITHOUT FEE IS HEREBY 
    GRANTED, PROVIDED THAT THE ABOVE COPYRIGHT NOTICE AND THIS PERMISSION NOTICE APPEAR IN ALL COPIES. THE SOFTWARE
    IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED
    WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, 
    INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS,
    WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE
    USE OR PERFORMANCE OF THIS SOFTWARE.
'''

# globals
password_length = random.randint(9, 15)          # total password string length
upper_case = random.randint(1, 3)                # total uppercase characters
special_chars = random.randint(1, 2)             # total special characters
num_numbers = random.randint(1, 2)               # total numbers


def generate():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    special_characters = "@#$%^&?"
    numbers = "0123456789"
    uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    password = ""
    for a in range(special_chars):
        special_char = random.choice(special_characters)
        password += special_char
    for b in range(num_numbers):
        number = random.choice(numbers)
        password += number
    for c in range(upper_case):
        upper = random.choice(uppers)
        password += upper
    for d in range(len(password), password_length):
        next_letter_index = random.choice(alphabet)
        password += next_letter_index
    password_list = list(password)
    random.shuffle(password_list)
    password_result = ''.join(password_list)
    return password_result


generate()
