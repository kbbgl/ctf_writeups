# Operation Orchid

## Description

Download [this disk image](https://artifacts.picoctf.net/c/236/disk.flag.img.gz) and find the flag.

## Investigation

```bash
❯ file disk.flag.img.gz
disk.flag.img.gz: gzip compressed data, was "disk.flag.img", last modified: Tue Mar 15 06:41:51 2022, from Unix, original size modulo 2^32 419430400

❯ gzip -d disk.flag.img.gz

❯ file disk.flag.img
disk.flag.img: DOS/MBR boot sector; partition 1 : ID=0x83, active, start-CHS (0x0,32,33), end-CHS (0xc,223,19), startsector 2048, 204800 sectors; partition 2 : ID=0x82, start-CHS (0xc,223,20), end-CHS (0x19,159,6), startsector 206848, 204800 sectors; partition 3 : ID=0x83, start-CHS (0x19,159,7), end-CHS (0x32,253,11), startsector 411648, 407552 sectors
```


## Mounting

```bash
❯ fdisk -l disk.flag.img
Disk disk.flag.img: 400 MiB, 419430400 bytes, 819200 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0xb11a86e3

Device         Boot  Start    End Sectors  Size Id Type
disk.flag.img1 *      2048 206847  204800  100M 83 Linux
disk.flag.img2      206848 411647  204800  100M 82 Linux swap / Solaris
disk.flag.img3      411648 819199  407552  199M 83 Linux
```

## Finding the Flag

```bash
❯ find ./ -type f -name "*flag*"
./root/flag.txt.enc
```

We can see that the flag is SALTed:
```bash
❯ cat ./root/flag.txt.enc
Salted__A)oBAqncb#>=D / >4ZȤ7 ؎$'%% 
```

But when attempting to decrypt, we're asked for a password:

```bash
❯ openssl des3 -d -in ./root/flag.txt.enc -out flag.txt
enter des-ede3-cbc decryption password:
```

I was able to find the password by:
```bash
❯ grep -rnwI "salt" ./* 2&> /dev/null | head -1
./root/.ash_history:8:openssl aes256 -salt -in flag.txt -out flag.txt.enc -k unbreakablepassword1234567
```

Decryption throws an error but the flag is there:
```bash
❯ openssl aes256 -d -in ./root/flag.txt.enc -out flag.txt -k unbreakablepassword1234567
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.
bad decrypt
140737348011328:error:06065064:digital envelope routines:EVP_DecryptFinal_ex:bad decrypt:../crypto/evp/evp_enc.c:610:

❯ cat flag.txt
picoCTF{h4un71ng_p457_0a710765}
```
