# Eavesdrop

## Description

Download [this packet](./capture.flag.pcap) capture and find the flag.


Opening the dump in Wireshark, we can see that there's some conversation going on. By following the TCP stream, we can read the whole exchange:

> Hey, how do you decrypt this file again?  
You're serious?  
Yeah, I'm serious  
```bash
openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123
```
> Ok, great, thanks.  
Let's use Discord next time, it's more secure.  
> C'mon, no one knows we use this program like this!  
> Whatever.  
> Hey.  
> Yeah?  
> Could you transfer the file to me again?  
> Oh great. Ok, over 9002?  
> Yeah, listening.  
> Sent it  
> Got it.  
> You're unbelievable  


So we know that the file will be sent over port `9002` and we know it's going to be encrypted using Triple DES cipher. 

Adding the filter `tcp.port == 9002` to Wireshark, we see that the following packet contains some data

```
57	205.302713	10.0.2.15	10.0.2.4	TCP	114	56370 → 9002 [PSH, ACK] Seq=1 Ack=1 Win=64256 Len=48 TSval=3517420532 TSecr=1765870695
```

If we export packet as bytes (CTRL + SHIFT + X), we get the file we need to feed into OpenSSL:

```bash
> openssl des3 -d -in wireshark_export.des3 -out flag.txt -k supersecretpassword123
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.

> cat flag.txt

picoCTF{nc_73115_411_5786acc3}
```