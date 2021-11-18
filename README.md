# ttbt
Command-line Top Text Bottom Text meme generator

## Features:
- Uses Impact font with stroke
- Supports line-wrapping
- Reads in .jpg, .png, or .gif images

## Usage:
- Either run the file directly, or add to your system PATH.
- Ex: ttbt path/to/image.jpg -t "Top Text" -b "Bottom Text"

To add to your system path on linux, simply copy the file to /usr/bin, and add the following line to the top of the file:
```
#!/usr/bin/env python
```
Also make sure to change the font import to point to the location of the impact.ttf file. Done!

## Deps:
- Python 3.9
- click >= 8.0.3
- Pillow >= 8.4.0
