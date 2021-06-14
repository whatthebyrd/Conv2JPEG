#!/usr/bin/env python3

# conv2jpg
# Invoke by: conv2jpeg <filename>
# Takes selected file and converts, if able, to .jpg
# Orignal Creation: 24NOV20
#  Released under Apache 2.0 License

import os # For checking file path and replacing file extension
import sys # For parsing input arguments 
from PIL import image # For image conversion

if sys.argv == True:
    if os.path.exists(sys.argv[1]):
        img2conv = Image.open(sys.argv[1])
        convimg_color = img2conv.convert("RGB")
        convimg_filename = os.path.splitext(sys.argv[1])[0] + '.jpg'
        convimg_color.save(convimg_filename)
        print(sys.argv[1] + " converted to " + convimg_filename + " successfully.")
    else:
        print("Error: \"" + sys.argv[1] + "\" file name not found. Exiting.")
else:
    print("Error: Target file required. Exiting.")
