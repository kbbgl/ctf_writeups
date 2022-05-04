#!/usr/bin/python3

import sys
import string

FLAG_PREFIX = "actf"
IGNORED_CHARS = ["_", "{", "}"]
ALPHABET = string.ascii_lowercase

def get_char_distance(c1: str, c2: str):

    """
    Helper function to calculate distance between letters

    Args:
        - `c1` (``str``): The first letter
        - `c2` (``str``): The second letter

    Returns:
        - `int` representing the distance between the letters
    """

    distance = ord(c2) - ord(c1)

    if distance < 0:
        distance = distance % len(ALPHABET)
    
    return distance

try:
    encrypted = sys.argv[1]

    distance = get_char_distance(encrypted[0], FLAG_PREFIX[0])

    flag = ""
    for i in range(len(encrypted)):
        letter_flag = encrypted[i]
        if letter_flag in IGNORED_CHARS:
            flag += letter_flag
            continue
        
        index = ALPHABET.index(letter_flag)

        decrypted_letter_index = index + distance
        if decrypted_letter_index >= len(ALPHABET):
            decrypted_letter_index = decrypted_letter_index % len(ALPHABET)

        decrypted_letter = ALPHABET[decrypted_letter_index]

        # decrypted_letter = chr(distance + ord(letter_flag))
        print(f"'{letter_flag}' + {distance} => {decrypted_letter}")
        flag += decrypted_letter

    print(flag)


except IndexError as ie:
    print("Error: Insufficient arguments")
    print("Usage: cipher.py TEXT_TO_DECRYPT")

except Exception as e:
    print(f"Error: {e}")