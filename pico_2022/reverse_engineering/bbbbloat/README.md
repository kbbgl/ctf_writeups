# Bbbbloat

## Description
Reverse engineer [this binary](https://artifacts.picoctf.net/c/301/bbbbloat)


## Reversing

We can see that the file is stripped, meaning it doesn't contain any debugging symbols.

```bash
> file bbbbloat

bbbbloat: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=99c5c1ce06be240322c15bcabc3cd90318eb2003, for GNU/Linux 3.2.0, stripped
```

Let's find the entrypoint and set a breakpoint there:

```bash
gdb bbbbloat

Reading symbols from bbbbloat...
(No debugging symbols found in bbbbloat)

(gdb) info file
Symbols from "bbbbloat".
Local exec file:
        `bbbbloat', file type elf64-x86-64.
        Entry point: 0x555555555160

(gdb) b *0x555555555160

        
```

Used Ghidra to open and analyze binary. Found value in one of the stripped functions.
