# Transformation

Given the following Python code:
```python
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
```

and a file containing UTF-8 encoded Chinese characters:

```bash
file enc&&cat enc
enc: UTF-8 Unicode text, with no line terminators
灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弲㘶㠴挲ぽ%
```



Let's break down the supplied Python code:

```
''.join(
	[
		chr((ord(flag[i]) << 8) + ord(flag[i + 1])) 
            for i in range(0, len(flag), 2)
	]
)
```

We can see that we can see that the flag is being encoded with the code above. It's encoding it by constructing a string by `join`ing a `list` of 2 characters (notice the last argument supplied to the `range` function). These pairs of characters are calculated by adding the the Unicode characters (returned by `ord` function) of the `n`th and `n + 1`th character. The `n`th character is shifted to the left by 8 bits before it's added.




This means that in order to get the flag, we would need to build a decoder