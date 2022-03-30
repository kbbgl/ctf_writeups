# Torrent 

## Description

SOS, someone is torrenting on our network.

One of your colleagues has been using torrent to download some files on the company’s network. Can you identify the file(s) that were downloaded? The file name will be the flag, like:

```
picoCTF{filename}
```

[Captured traffic](https://artifacts.picoctf.net/c/206/torrent.pcap)


Found the info_hash in packet 51080, used it in torrent client to download the file.

```
picoCTF{ubuntu-19.10-desktop-amd64.iso}
```

### Sources

- https://ask.wireshark.org/question/13516/looking-for-a-file/
