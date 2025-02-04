import string

# Generate the allowed characters
all_available_chars = list(string.ascii_letters + string.punctuation + string.digits + " ")
char_set_length = len(all_available_chars)

# Precompute a dictionary for fast character lookup
char_to_index = {char: i for i, char in enumerate(all_available_chars)}


def transform_message(message, shift):
    """
    Transform the message by applying a shift.
    A positive shift encodes, negative - decodes.
    Characters not in the allowed set remain unchanged
    """

    output_chars = []
    for char in message:
        index = char_to_index.get(char)
        if index is not None:
            new_index = (index + shift) % char_set_length
            output_chars.append(all_available_chars[new_index])
        else:
            output_chars.append(char)
    return ''.join(output_chars)


def encode(cipher_nr):
    """Encode a message using the specified cipher number."""
    input_message = get_message("Type the message that you would like to encode: ")
    encoded_message = transform_message(input_message, cipher_nr)
    return input_message, encoded_message


def decode(cipher_nr):
    """Decode a message using the specified cipher number."""
    input_message = get_message("Type the message that you would like to decode: ")
    decoded_message = transform_message(input_message, -cipher_nr)
    return input_message, decoded_message


def get_message(prompt):
    """Prompt the user to enter a message."""
    return input(prompt).strip()


def get_cipher_number(prompt):
    """
    Prompt the user for a valid cipher number ( a positive, non-zero integer).
    Returns the cipher number reduced modulo the number of allowed characters.
    """

    while True:
        user_input = input(prompt).strip()
        if not user_input.isdigit():
            print("Invalid input. Please enter a positive non-zero number.")
            continue
        cipher_number = int(user_input)
        if cipher_number == 0:
            print("The cipher number must be greater than 0.")
            continue
        return cipher_number % char_set_length


def get_operation():
    """
    Ask the user whether they want to encode or decode.
    Returns 'e' for encoding, 'd' for decoding.
    """
    while True:
        op = input("Type 'e' for encoding or 'd' for decoding: ").strip().casefold()
        if op in ['e', 'd']:
            return op
        print("Please enter 'e' for encoding or 'd' for decoding!")


def get_decode_or_encode():
    """
    Determine whether the user wants to encode or decode,
    prompt for the cipher number, and process the message accordingly.
    Returns the original message, the processed message and the operation type.
    """
    operation = get_operation()
    cipher_number = get_cipher_number("Enter the cipher number: ")
    if operation == 'e':
        original, processed = encode(cipher_number)
    else:
        original, processed = decode(cipher_number)

    return original, processed, cipher_number


def main():
    print("Welcome to the Caesar Cipher program!")

    while True:
        original_message, output_message, operation = get_decode_or_encode()
        if operation == 'e':
            print(f"\nThe original message: {original_message}")
            print(f"The encoded message:  {output_message}\n")
        else:
            print(f"\nThe original message: {original_message}")
            print(f"The decoded message:  {output_message}\n")

        cont = input("To continue, enter 'Y'. Any other key to exit: ").strip().casefold()
        if cont != 'y':
            print("Goodbye, traveler!")
            break


if __name__ == '__main__':
    main()
