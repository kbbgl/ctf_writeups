# `credstuf`

## Description

We found a leak of a blackmarket website's login credentials. 
Can you find the password of the user `cultiris` and successfully decrypt it?

Download the leak [here](https://artifacts.picoctf.net/c/534/leak.tar).

The first user in `usernames.txt` corresponds to the first password in `passwords.txt`. The second user corresponds to the second password, and so on.


## Research

We can find what line the username `cultiris` is in by using `awk`:

```bash
awk '/cultiris/{ print NR; exit }' usernames.txt
378
```

Let's see what's printed in this line in the passwords file:

```bash
sed -n 378p passwords.txt
cvpbPGS{P7e1S_54I35_71Z3}
```

In line 204, we find:

```bash
sed -n 204p usernames.txt
pico

sed -n 204p passwords.txt
pICo7rYpiCoU51N6PicOr0t13
```

If we look at the last 5 characters of the password in line 204, `r0t13`, we see that there's a hint as to what type of cipher is used to encrypt the password, namely ROT13. It basically replaces the letter in the sequence with a letter 13 characters up in the alphabet.

![](https://upload.wikimedia.org/wikipedia/commons/2/2a/ROT13.png)

Since we know that the expected flag format is `picoCTF{SOMEFLAG}`, we can test out the ROT13 with the first few letters:

```
c + 13 = p
v - 13 = i
p - 13 = c
b + 13 = o
```

We can use the built-in Python ROT13 decoder to get the flag:

```python
import codecs
codecs.decode('cvpbPGS{P7e1S_54I35_71Z3}', 'rot_13')
'picoCTF{C7r1F_54V35_71M3}'
```