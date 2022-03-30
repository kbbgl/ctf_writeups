#!/usr/bin/python3


with open('./enc') as f:
    chinese = f.readline()


for i in range(0, len(chinese), 2):

   print(chr((ord(chinese[i]) << 8) + ord(chinese[i + 1])))



# ''.join([chr((ord(chinese[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
