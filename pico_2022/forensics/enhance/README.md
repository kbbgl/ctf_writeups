# Enhance!


## Description
https://play.picoctf.org/events/70/challenges/challenge/265

Download [this image file](https://artifacts.picoctf.net/c/136/drawing.flag.svg) and find the flag.


## Research

We can see that the file is a SVG:

```bash
file drawing.flag.svg
drawing.flag.svg: SVG Scalable Vector Graphics image
```

Since SVG is basically a vector-based graphics printed in XML format, it's not encoded so we can print it out as a regular text file.

If we look at the XML, we can see that the flag is contained with `tspan` nodes which are children of the `text` node. The `text` node is a 3rd child of `g` node which is a 3rd child of the `root`.

We can use Python to parse the SVG and get the flag.


```python
import xml.etree.ElementTree as ET
tree = ET.parse('drawing.flag.svg')
root = m_tree.getroot()

flag = ""                                            
for s in root[3].getchildren()[3].getchildren():
    flag += s.text.replace(" ", "")                  

print(flag)
# picoCTF{3nh4nc3d_aab729dd}
```