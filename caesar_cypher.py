from caesar_cypher_art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(plain_text, shift_amount, the_direction):
    cipher_text = ""
    new_position = 0
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if the_direction == "encode":
                new_position = position + shift_amount
                if new_position >= 26:
                    new_position -= 26
            elif the_direction == "decode":
                new_position = position - shift_amount
                if new_position < 0:
                    new_position += 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter   # same character and position
    print(f"The {the_direction}d text is {cipher_text}")


print(logo)
not_finished = True
while not_finished:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(plain_text=text, shift_amount=(shift % 26), the_direction=direction)
    result = input("Continue? [Y/N] ")
    if result.lower() == "y":
        not_finished = True
    else:
        not_finished = False


