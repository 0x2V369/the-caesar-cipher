# Caesar Cipher

def encode(message, shift_number):
    """
    Encode the message using the Caesar cipher technique.

    :param message: The message to be encoded
    :param shift_number: The number of positions to shift each letter
    """
    encoded_message = []

    for letter in message:
        if letter in ALPHABET:
            index = (ALPHABET.index(letter) + shift_number) % 26
            encoded_message.append(ALPHABET[index])
        else:
            encoded_message.append(letter)  # Keep non-alphabet chars unchanged

    print("Your encoded message is: {}".format(''.join(encoded_message)))


def decode(message, shift_number):
    """
    Decode the message using the Caesar cipher technique.

    :param message: The message to be decoded
    :param shift_number: The number of positions to shift each letter back
    """
    decoded_message = []

    for letter in message:
        if letter in ALPHABET:
            index = (ALPHABET.index(letter) - shift_number) % 26
            decoded_message.append(ALPHABET[index])
        else:
            decoded_message.append(letter)  # Keep non-alphabet chars unchanged

    print("Your decoded message is: {}".format(''.join(decoded_message)))


def get_user_choice():
    """
    Get the user's choice to encode or decode.

    :return: 'encode' or 'decode' based on the user's input
    """
    while True:
        choice = str(input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")).casefold()
        if choice in ['encode', 'decode']:
            return choice
        else:
            print("Invalid choice, please try again.")


def get_user_message():
    """
    Get the message from the user.

    :return: The user's message in lowercase
    """
    return input("Type your message:\n").casefold()


def get_shift_number():
    """
    Get the shift number from the user.

    :return: The shift number as an integer
    """
    while True:
        try:
            shift = int(input("Type the shift number:\n"))
            return shift
        except ValueError:
            print("Invalid number, please enter an integer.")


# Define the alphabet used in the Caesar cipher
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# List of affirmative responses for continuing the program
affirmative = ['y', 'yea', 'yes', 'yeah']

# Main loop to keep the program running
keep_running = True

while keep_running:

    choice = get_user_choice()  # Get user's choice to encode or decode
    message = get_user_message()  # Get the message from the user
    shift_number = get_shift_number()  # Get the shift number from the user

    if choice == 'encode':
        encode(message, shift_number)  # Encode the message
    else:
        decode(message, shift_number)  # Decode the message

    to_continue = input("Would you like to continue? (yes/no)\n").casefold()
    if to_continue not in affirmative:
        keep_running = False  # Stop the program if the user doesn't want to continue
