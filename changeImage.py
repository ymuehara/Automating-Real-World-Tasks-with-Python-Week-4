#!/usr/bin/env python3

# https://pillow.readthedocs.io/en/stable/

from PIL import Image
import os

path = "supplier-data/images/"
pictures = os.listdir(path)

for pic in pictures:
  if 'tiff' in pic:
    file_name = os.path.splitext(pic)[0]
    outfile = "supplier-data/images/" + file_name + ".jpeg"
    img = Image.open(path + pic)
    img.convert("RGB").resize((600,400)).save(outfile, "JPE")
    img.close()

