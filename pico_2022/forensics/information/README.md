# Information

The [image](cat.jpg) included an attribute that had the flag in `base64`. Used [`exiftool`](https://exiftool.org/) to look at license:

```bash
./exiftool ../cat.jpg | grep License | cut -d":" -f2 | tr -d "[:space:]" | base64 -d
```

Source: https://medium.com/@andr3w_hilton/brain-gamez-ctf-1f66cebc7355