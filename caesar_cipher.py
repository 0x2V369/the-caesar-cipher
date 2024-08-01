# Caesar Cipher

def encode(message, shift_number):
    encoded_message = []

    for letter in message:
        if letter in ALPHABET:
            index = (ALPHABET.index(letter) + shift_number) % 26
            encoded_message.append(ALPHABET[index])
        else:
            encoded_message.append(letter)  # Keep non-alphabet chars unchanged

    print("Your encoded message is: {}".format(''.join(encoded_message)))


def decode(message, shift_number):
    decoded_message = []

    for letter in message:
        if letter in ALPHABET:
            index = (ALPHABET.index(letter) - shift_number) % 26
            decoded_message.append(ALPHABET[index])
        else:
            decoded_message.append(letter)  # Keep non-alphabet chars unchanged

    print("Your decoded message is: {}".format(''.join(decoded_message)))


def get_user_choice():
    while True:
        choice = str(input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")).casefold()
        if choice in ['encode', 'decode']:
            return choice
        else:
            print("Invalid choice, please try again.")


def get_user_message():
    return input("Type your message:\n").casefold()


def get_shift_number():
    while True:
        try:
            shift = int(input("Type the shift number:\n"))
            return shift
        except ValueError:
            print("Invalid number, please enter an integer.")


ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

affirmative = ['y', 'yea', 'yes', 'yeah']

keep_running = True

while keep_running:

    choice = get_user_choice()
    message = get_user_message()
    shift_number = get_shift_number()

    if choice == 'encode':
        encode(message, shift_number)
    else:
        decode(message, shift_number)

    to_continue = input("Would you like to continue? (yes/no)\n").casefold()
    if to_continue not in affirmative:
        keep_running = False
