
---

# Caesar Cipher

A Python implementation of the classic Caesar cipher encryption technique. This project provides two implementations:

- **Original Version (V1):**  
  A basic version that uses a predefined lowercase alphabet. It supports encoding and decoding of messages while leaving non-alphabet characters unchanged.

- **Improved Version (V2):**  
  A refactored and optimized version that:
  - Supports a broader set of characters (letters, digits, punctuation, and space).
  - Uses a precomputed dictionary for fast character lookups.
  - Efficiently builds output strings using list appends and the `join()` method.
  - Consolidates common encoding/decoding logic in a single transformation function.
  - Includes enhanced input validation and a more modular design.

> **Note:** V2 is the recommended version as it offers improved performance and flexibility.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the Original Version (V1)](#running-the-original-version-v1)
  - [Running the Improved Version (V2)](#running-the-improved-version-v2)
- [Code Overview](#code-overview)
  - [Original Version (V1)](#original-version-v1)
  - [Improved Version (V2)](#improved-version-v2)
- [Changelog](#changelog)
- [License](#license)
- [Author](#author)

## Features

- **Encoding and Decoding:**  
  Easily shift messages by a user-specified number to encrypt or decrypt text.
  
- **Input Validation:**  
  Ensures valid input for both the message and the shift number.
  
- **Support for Non-Alphabet Characters:**  
  - **V1:** Keeps non-alphabet characters unchanged.  
  - **V2:** Supports a full range of characters (letters, punctuation, digits, and space) and leaves unsupported characters unchanged.
  
- **Optimizations in V2:**  
  - Fast character lookup using a precomputed dictionary.
  - Efficient string construction using list appends and `join()`.
  - Consolidated transformation logic for encoding and decoding.

## Requirements

- Python 3.x (tested on Python 3.8+)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/caesar-cipher.git
   cd caesar-cipher
   ```

2. **(Optional) Create a Virtual Environment:**

   ```bash
   python -m venv env
   source env/bin/activate   # On Windows, use: env\Scripts\activate
   ```

## Usage

### Running the Original Version (V1)

1. **Navigate to the V1 file (e.g., `caeser_cipher.py`).**
2. **Run the Program:**

   ```bash
   python caeser_cipher.py
   ```

3. **Follow the Prompts:**

   - Choose whether to encode or decode.
   - Enter your message (note: V1 processes only lowercase letters).
   - Enter the shift number.

   **Example:**
   ```
   Type 'encode' to encrypt, type 'decode' to decrypt:
   encode
   Type your message:
   hello world
   Type the shift number:
   3
   Your encoded message is: khoor zruog
   ```

### Running the Improved Version (V2)

1. **Navigate to the V2 file (e.g., `caeser_cipher_v2.py`).**
2. **Run the Program:**

   ```bash
   python caeser_cipher_v2.py
   ```

3. **Follow the Prompts:**

   - Choose whether to encode (`e`) or decode (`d`).
   - Enter your message.
   - Enter the cipher (shift) number.
   
   **Example:**
   ```
   Welcome to the Caesar Cipher program!
   Type 'e' for encoding or 'd' for decoding: e
   Enter the cipher number: 5
   Type the message that you would like to encode: Hello, World!
   
   The original message: Hello, World!
   The encoded message:  Mjqqt1%Btwqi&
   
   To continue, enter 'Y'. Any other key to exit:
   y
   ```

## Code Overview

### Original Version (V1)

- **Files:**  
  - `caeser_cipher.py`
  
- **Key Functions:**
  - `encode(message, shift_number)`: Shifts each character in the message (if it exists in a predefined lowercase alphabet) by the given shift number.
  - `decode(message, shift_number)`: Shifts characters in the opposite direction to decrypt.
  - `get_user_choice()`, `get_user_message()`, and `get_shift_number()`: Handle user input and validation.
  
- **Alphabet:**  
  Uses a list of lowercase alphabetic characters (`a` to `z`).

- **Main Loop:**  
  Continuously processes user requests until the user opts to exit.

### Improved Version (V2)

- **Files:**  
  - `caeser_cipher_v2.py`
  
- **Key Improvements:**
  - **Flexible Character Set:**  
    Uses a list of allowed characters that includes uppercase and lowercase letters, punctuation, digits, and space.
  
  - **Optimized Lookup:**  
    A precomputed dictionary (`char_to_index`) is used for constant-time lookup of character positions.
  
  - **Efficient String Construction:**  
    Instead of concatenating strings in a loop, characters are appended to a list and then joined into the final string.
  
  - **Unified Transformation:**  
    The `transform_message(message, shift)` function applies the shift (positive for encoding, negative for decoding) to reduce redundancy between `encode()` and `decode()`.
  
- **Additional Functions:**  
  - `get_message()`, `get_cipher_number()`, and `get_operation()` handle input validation and streamline the user interaction process.
  
- **Program Flow:**  
  Uses a main loop that continuously allows the user to encode or decode messages until they decide to exit.

### Core Excerpt from V2

```python
import string

# Generate the allowed characters and precompute lookup dictionary
all_available_chars = list(string.ascii_letters + string.punctuation + string.digits + " ")
char_set_length = len(all_available_chars)
char_to_index = {char: i for i, char in enumerate(all_available_chars)}

def transform_message(message, shift):
    """
    Transform the message by applying a shift.
    A positive shift encodes; a negative shift decodes.
    Characters not in the allowed set remain unchanged.
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
```

## Changelog

- **V1:**  
  - Basic Caesar Cipher implementation.
  - Processes only lowercase alphabetic characters.
  - Uses linear search with `list.index()`.

- **V2:**  
  - Extended support for a full character set (letters, punctuation, digits, and space).
  - Optimized using a precomputed dictionary for faster character lookup.
  - Efficient string building with list operations.
  - Consolidated logic via the `transform_message` function.
  - Enhanced input validation and overall modularity.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

This Caesar Cipher implementation was developed by [0x2V369](https://github.com/0x2V369).
```

---

Feel free to modify any sections (like repository URLs or file names) to suit your project's specific structure and needs. Enjoy coding and happy encrypting!