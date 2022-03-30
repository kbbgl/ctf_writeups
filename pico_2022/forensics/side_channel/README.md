# SideChannel

## Description
There's something fishy about this PIN-code checker, can you figure out the PIN and get the flag?

Download the PIN checker program [here](https://artifacts.picoctf.net/c/143/pin_checker) `pin_checker`.

Once you've figured out the PIN and gotten the checker program to accept it, connect to the master server using 

```bash
nc saturn.picoctf.net 55824
```

and provide it the PIN to get your flag.


## Investigation

```bash
❯ file pin_checker
pin_checker: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, stripped
```

## Finding the PIN

From the hints we know that we're supposed to attempt a time-based side channel attack on the binary to get the PIN.

Using the `time` tool, and observing the increasing amount of total time it took for the binary to return a response while changing the PIN 1 digit at a time between `0-9`, I was able to find that the PIN was:

```bash
❯ time echo "48390513" | ./pin_checker
Please enter your 8-digit PIN code:
8
Checking PIN...
Access granted. You may use your PIN to log into the master server.
echo "48390513"  0.00s user 0.00s system 57% cpu 0.001 total
./pin_checker  1.22s user 0.02s system 99% cpu 1.242 total
```

From there it was easy to get the flag:

```bash
❯ echo 48390513 | nc saturn.picoctf.net 55824
Verifying that you are a human...
Please enter the master PIN code:
Password correct. Here's your flag:
picoCTF{t1m1ng_4tt4ck_9803bd25}
```