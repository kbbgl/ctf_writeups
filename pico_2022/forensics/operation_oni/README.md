# Operation Oni

## Description

Download [this disk image](https://artifacts.picoctf.net/c/373/disk.img.gz), find the key and log into the remote machine.

Remote machine: 

```bash
ssh -i key_file -p 59356 ctf-player@saturn.picoctf.net
```

## Research

```bash
file disk.img.gz
disk.img.gz: gzip compressed data, was "disk.img", last modified: Wed Oct  6 14:32:01 2021, from Unix, original size modulo 2^32 241172480

gunzip disk.img.gz

❯ ls
disk.img

❯ sudo mkdir /mnt/pico

❯ sudo mount -o loop disk.img /mnt/pico
mount: /mnt/pico: wrong fs type, bad option, bad superblock on /dev/loop21, missing codepage or helper program, or other error.

❯ file disk.img
disk.img: DOS/MBR boot sector; partition 1 : ID=0x83, active, start-CHS (0x0,32,33), end-CHS (0xc,223,19), startsector 2048, 204800 sectors; partition 2 : ID=0x83, start-CHS (0xc,223,20), end-CHS (0x1d,81,52), startsector 206848, 264192 sectors

❯ fdisk -l disk.img
Disk disk.img: 230 MiB, 241172480 bytes, 471040 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x0b0051d0

Device     Boot  Start    End Sectors  Size Id Type
disk.img1  *      2048 206847  204800  100M 83 Linux
disk.img2       206848 471039  264192  129M 83 Linux
```

So we know that there are two partitions on this disk. Let's look in `disk.img2` as it seems that the first disk is actually used for boot.

In order to mount the device, we need to supply the offset (5012 bytes * 206848 = 105906176):

```bash
❯ sudo mount -o loop,offset=$((512*206848)),sizelimit=$((512*264192)) disk.img /mnt/pico
❯ sudo mount -o loop,offset=$((512*2048)),sizelimit=$((512*204800)) disk.img /mnt/pico2
```

Found the key and got access to the remote server:

```bash
❯ sudo find ./ -type f -name "*.pub" | head -n1
./root/.ssh/id_ed25519.pub
❯ ssh -i ./root/.ssh/id_ed25519 -F /dev/null -p 57884 ctf-player@saturn.picoctf.net
ssh: connect to host saturn.picoctf.net port 57884: Connection refused
❯ ssh -i ./root/.ssh/id_ed25519 -F /dev/null -p 56519 ctf-player@saturn.picoctf.net
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.13.0-1017-aws x86_64)


ctf-player@challenge:~$ ls
flag.txt
ctf-player@challenge:~$ cat flag.txt 
picoCTF{k3y_5l3u7h_b5066e83}ctf-player@challenge:~$ Connection to saturn.picoctf.net closed by remote host.
Connection to saturn.picoctf.net closed.
```

### Sources

- https://www.linuxquestions.org/questions/linux-software-2/how-to-mount-dos-img-file-4175430554/
- https://forums.raspberrypi.com/viewtopic.php?t=190154