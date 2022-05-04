# Confetti

Points: 40
Category: [Steganography](https://fareedfauzi.gitbook.io/ctf-checklist-for-beginner/steganography)

## Description
"From the sky, drop like confetti All eyes on me, so V.I.P All of my dreams, from the sky, drop like confetti" - Little Mix

[confetti](https://files.actf.co/bcf3009b7dc908d24847db01790891ce8453e900fa0b15f1f214f5392c1aabd4/confetti.png)


## Enumeration

```bash
file confetti.png

confetti.png: PNG image data, 3971 x 2918, 8-bit/color RGBA, non-interlaced
```

I then used `binwalk` to check if there were any hidden files inside the image

```bash
binwalk confetti.png

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 3971 x 2918, 8-bit/color RGBA, non-interlaced
115           0x73            Zlib compressed data, default compression
967339        0xEC2AB         PNG image, 3971 x 2918, 8-bit/color RGBA, non-interlaced
967454        0xEC31E         Zlib compressed data, default compression
1934678       0x1D8556        PNG image, 3971 x 2918, 8-bit/color RGBA, non-interlaced
1934732       0x1D858C        TIFF image data, big-endian, offset of first image directory: 8
3180408       0x308778        PNG image, 3971 x 2918, 8-bit/color RGBA, non-interlaced
3180523       0x3087EB        Zlib compressed data, default compression
```

We can see that there are some more images and compressed archives. Let's extract them into the filesystem:

```bash
binwalk --dd=".*" -C="$(pwd)/extracted"  confetti.png

ll ./extracted/_confetti.png.extracted

total 21M
-rw-rw-r-- 1 kobbi kobbi 4.0M May  4 15:03 0
-rw-rw-r-- 1 kobbi kobbi 2.2M May  4 15:03 1D8556
-rw-rw-r-- 1 kobbi kobbi 2.2M May  4 15:03 1D858C
-rw-rw-r-- 1 kobbi kobbi 945K May  4 15:03 308778
-rw-rw-r-- 1 kobbi kobbi    0 May  4 15:03 3087EB
-rw-rw-r-- 1 kobbi kobbi 945K May  4 15:03 3087EB-0
-rw-rw-r-- 1 kobbi kobbi    0 May  4 15:03 73
-rw-rw-r-- 1 kobbi kobbi 4.0M May  4 15:03 73-0
-rw-rw-r-- 1 kobbi kobbi 3.1M May  4 15:03 EC2AB
-rw-rw-r-- 1 kobbi kobbi    0 May  4 15:03 EC31E
-rw-rw-r-- 1 kobbi kobbi 3.1M May  4 15:03 EC31E-0
```

If we look at the `1D8556` in an image viewer, we see the flag:

```bash
file extracted/_confetti.png.extracted/1D8556
extracted/_confetti.png.extracted/1D8556: PNG image data, 3971 x 2918, 8-bit/color RGBA, non-interlaced

eog 1D8556
```