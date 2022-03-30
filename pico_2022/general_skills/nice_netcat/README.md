# Nice Netcat

The server returns a number per line, each number is an ASCII representation:

```bash
# write response to file
nc mercury.picoctf.net 22902 > nc.ascii 2>&1

# read it line by line and convert ASCII number to character and save to file 
while read -r line; do echo "\x$(printf %x $line)"; done < nc.ascii | tr -d "\n"
 ```