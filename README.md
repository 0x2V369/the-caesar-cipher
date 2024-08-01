# Caesar Cipher

This is a simple implementation of the Caesar cipher in Python. The Caesar cipher is a basic encryption technique where each letter in the plaintext is shifted a certain number of places down the alphabet.

## Features

- **Encoding and Decoding**: Allows the user to encode and decode messages using a specified shift number.
- **Input Validation**: Ensures that the user inputs valid characters and numbers.
- **Support for Non-Alphabet Characters**: Keeps spaces and punctuation unchanged in the encoded/decoded messages.

## Requirements

- Python 3.x

## How to Use

1. **Clone the Repository:**
    ```sh
    git clone https://github.com/0x2V369/the-caesar-cipher.git
    cd caesar-cipher
    ```

2. **Run the Program:**
    ```sh
    python caesar_cipher.py
    ```

3. **Follow the Instructions:**
    - Choose whether to encode or decode a message.
    - Enter the message to be encoded or decoded.
    - Enter the shift number.

4. **Example Usage:**
    ```
    Type 'encode' to encrypt, type 'decode' to decrypt:
    encode
    Type your message:
    hello world
    Type the shift number:
    3
    Your encoded message is: khoor zruog
    ```

## Code Overview

### Functions

- `encode(message, shift_number)`: Encodes the given message using the specified shift number.
- `decode(message, shift_number)`: Decodes the given message using the specified shift number.
- `get_user_choice()`: Prompts the user to choose between encoding and decoding.
- `get_user_message()`: Prompts the user to enter a message.
- `get_shift_number()`: Prompts the user to enter the shift number.

### Alphabet

The program uses a list of lowercase alphabetic characters to perform the shifting operations.

### Main Loop

The program runs in a loop, allowing the user to encode or decode multiple messages until they choose to exit.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

This Caesar cipher implementation was developed by [0x2V369](https://github.com/0x2V369).
