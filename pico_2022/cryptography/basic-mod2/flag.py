#!/usr/bin/python3
import string

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None  # modular inverse does not exist
    else:
        return x % m


# Read message into variable
with open('./message.txt') as f:
    msg = f.readline()

# Message arrives as split strings
# Take all except last split as it is an empty string
msg_str_list = msg.split(' ')[:-1]

# Convert string from message into list of integers
msg_int_list = [int(x) for x in msg_str_list]

# take the modular inverse of every integer with modulu 41
result = [modinv(a, 41) for a in msg_int_list]

# Build character set
# 1 - 26 are the alphabet
# 27 - 36 are decimal digits
# 37 is _

char_set = list(string.ascii_lowercase)

for n in range(0, 10):
    char_set.append(str(n))

char_set.append("_")

# Insert at index 0 to push all elements up by 1
char_set.insert(0, 'None')

decrypted_message = ""

for integer in result:
    char = str(char_set[integer])
    decrypted_message += char

print("picoCTF{" + decrypted_message  + "}")
