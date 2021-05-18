#!/usr/bin/env python3
import ST7735
from PIL import Image, ImageDraw, ImageFont
from fonts.ttf import RobotoMedium as UserFont

# Create LCD class instance.
disp = ST7735.ST7735(
    port=0,
    cs=1,
    dc=9,
    backlight=12,
    rotation=270,
    spi_speed_hz=10000000
)

# initialize display
disp.begin()
WIDTH = disp.width
HEIGHT = disp.height

# initialize new canvas to draw on
img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))
draw = ImageDraw.Draw(img)
back_colour = (5, 5, 5)
draw.rectangle((0, 0, 160, 80), back_colour)

name = "Dennis Grigaliunas\n" \
       "Olivier Sips\n" \
       "Simon Masschelein\n" \
       "Souheil Allaoui"

# font settings
font_size = 12
font = ImageFont.truetype(UserFont, font_size)
text_colour = (255, 0, 0)

# text size
size_x, size_y = draw.textsize(name, font)

# text position
x = (WIDTH - size_x) / 2
y = (HEIGHT / 2) - (size_y / 2)

# write text to image
draw.text((x, y), name, font=font, fill=text_colour)
disp.display(img)


def stop():
    disp.set_backlight(0)
