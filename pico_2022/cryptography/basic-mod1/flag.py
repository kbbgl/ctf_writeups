#!/usr/bin/python3

import string
from typing import List


# Read file
with open('./message.txt') as f:
    msg = f.readline()

# Remove the last list element as it contains
# empty str
msg_str_list: List[str] = msg.split(' ')[:-1]

# Convert to list of integers and take modulus of 37
msg_int_list: List[int] = [int(x) % 37 for x in msg_str_list]


# Build character set
# 0  - 25 are uppercase alphabet letters
# 26 - 35 are decimal digits
# 36      underscore

char_set = list(string.ascii_uppercase) 

for n in range(0, 10):
    char_set.append(n)

char_set.append("_")

decrypted_message: str = ""

for integer in msg_int_list:
    char = str(char_set[integer])
    decrypted_message += char

print("picoCTF{" + decrypted_message + "}")