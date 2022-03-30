# St3g0

## Description
Download this [image](https://artifacts.picoctf.net/c/421/pico.flag.png) and find the flag

## Investigation

Used `zsteg` to find the flag:

```bash
❯ zsteg -a pico.flag.png                                                                                                                
b1,r,lsb,xy         .. text: "~__B>wV_G@"                                                                                               
b1,g,lsb,xy         .. file: dBase III DBT, version number 0, next free block index 3549684369                                          
b1,g,msb,xy         .. file: dBase III DBT, version number 0, next free block index 3418965897                                          
b1,b,lsb,xy         .. file: dBase III DBT, version number 0, next free block index 2623130757                                          
b1,rgb,lsb,xy       .. text: "picoCTF{7h3r3_15_n0_5p00n_96ae0ac1}$t3g0" 
```