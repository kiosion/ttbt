# Imports
import click
import textwrap
from PIL import Image, ImageFont, ImageDraw

@click.command()
@click.argument('image')
@click.option('-t')
@click.option('-b')

def main(image, t, b):

    if image is None:
        print ("Please provide path to an image!")
        exit()
    if t is None:
        t = ""
    if b is None:
        b = ""

    print("Top caption: " + t)
    print("Bottom caption: " + b)
    img = Image.open(image)
    W, H = img.size
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("assets/impact.ttf", size=int(H/14))

    offset = 0
    for line in textwrap.wrap(t, width=int(W-W/1.009)):
        w, h = draw.textsize(line, font=font)
        draw.text(((W-w)/2,offset), line, fill="white", stroke_width=int((H/14)/16), stroke_fill="black", font=font)
        offset += font.getsize(line)[1]

    offset = H
    for line in textwrap.wrap(b, width=int(W-W/1.009)):
        w, h = draw.textsize(line, font=font)
        offset -= font.getsize(line)[1]
    for line in textwrap.wrap(b, width=int(W-W/1.009)):
        w, h = draw.textsize(line, font=font)
        draw.text(((W-w)/2,offset), line, fill="white", stroke_width=int((H/14)/16), stroke_fill="black", font=font)
        offset += font.getsize(line)[1]

    img.save(image + '_out.png')
    print("Image saved!")

if __name__ == "__main__":
    main()
