# Caesar and Desister

Points: 40

## Description

After making dumb jokes about cryptography to all his classmates, clam got a cease and desist filed against him! When questioned in court, his only comment was "clam's confounding Caesar cipher creates confusing cryptographic challenges." Needless to say, the judge wasn't very happy. Clam was sentenced to 5 years of making dumb Caesar cipher challenges. Here's one of them: 

```
sulx{klgh_jayzl_lzwjw_ujqhlgyjshzwj_kume}
```

Wrote [a script](./cipher.py) to generate the decryption:

```bash
./cipher.py

Trying to decipher sulx{klgh_jayzl_lzwjw_ujqhlgyjshzwj_kume}...
's' + 8 => a
'u' + 8 => c
'l' + 8 => t
'x' + 8 => f
'k' + 8 => s
'l' + 8 => t
'g' + 8 => o
'h' + 8 => p
'j' + 8 => r
'a' + 8 => i
'y' + 8 => g
'z' + 8 => h
'l' + 8 => t
'l' + 8 => t
'z' + 8 => h
'w' + 8 => e
'j' + 8 => r
'w' + 8 => e
'u' + 8 => c
'j' + 8 => r
'q' + 8 => y
'h' + 8 => p
'l' + 8 => t
'g' + 8 => o
'y' + 8 => g
'j' + 8 => r
's' + 8 => a
'h' + 8 => p
'z' + 8 => h
'w' + 8 => e
'j' + 8 => r
'k' + 8 => s
'u' + 8 => c
'm' + 8 => u
'e' + 8 => m
actf{stop_right_there_cryptographer_scum}
```