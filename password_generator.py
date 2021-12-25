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
password_length = 12         # total password string length
upper_max_total = 3          # maximum total uppercase characters
upper_min_total = 1          # minimum total uppercase characters
special_char_max_total = 2   # maximum total special characters
special_char_min_total = 1   # minimum total special characters
number_max_total = 2         # maximum total numbers
number_min_total = 1         # minimum total numbers


def generate():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    special_characters = "@#$%^&?"
    numbers = "0123456789"
    uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    password = ""
    for a in range(random.randint(special_char_min_total, special_char_max_total)):
        special_char = special_characters[random.randint(0, len(special_characters)-1)]
        # print(f"special char {(a + 1)}: {special_char}")
        password += special_char
    for b in range(random.randint(number_min_total, number_max_total)):
        number = numbers[random.randint(0, len(numbers)-1)]
        # print(f"      number {(b + 1)}: {number}")
        password += number
    for c in range(random.randint(upper_min_total, upper_max_total)):
        upper = uppers[random.randint(0, len(uppers)-1)]
        # print(f"       upper {(c + 1)}: {upper}")
        password += upper
    for d in range(len(password), password_length):
        next_letter_index = random.randrange(len(alphabet))
        password += alphabet[next_letter_index]
    password_list = list(password)
    random.shuffle(password_list)
    password_result = (''.join(password_list))
    # print(f"      Password: {password_result}")
    return password_result


generate()
