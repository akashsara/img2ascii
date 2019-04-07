#!python3

import sys
import argparse
import os
import math
import numpy as np
from PIL import Image

def validate_path(location):
    """
    Just checks if the image exists in the given path.
    """
    return os.path.exists(location)

def load_image(location):
    """
    Loads an image, resizes it to 512, 512 (but maintains aspect ratio) and returns it as a 2D pixel matrix.
    If image can't be laoded, it returns an error and stops execution.
    """
    if validate_path(location):
        image = Image.open(location)
        print('Image loaded successfully. Processing...')
        image.thumbnail((512, 512), Image.ANTIALIAS)
        width, height = image.size
        print(f'Scaled Image Size: {width} x {height}')
        pixels = np.array(image, dtype='int64')
        return pixels
    else:
        print("That doesn't seem to be a valid image. Please check the given path.")
        sys.exit()

def rgb_to_brightness(image, mode):
    """
    Converts each image into a brightness scale depending on the given mode.
    Average: Averages the value of RGB
    Min_Max: Takes the average of the highest and lowest values from RGB.
    Luminosity: Uses a formula taken from the StackOverflow link below to get the 'perceived' brightness
    Max: Just take the max of RGB
    Min: Just take the min of RGB
    https://stackoverflow.com/questions/596216/formula-to-determine-brightness-of-rgb-color
    Basically just applies the given function to the entire image.
    """
    modes = {
        'average': lambda column:sum(column) // len(column),
        'min_max': lambda column:(max(column) + min(column)) // 2,
        'luminosity': lambda column: math.floor((0.21 * column[0]) + (0.72 * column[1]) + (0.07 * column[2])),
        'max': lambda column:max(column),
        'min': lambda column:min(column)
    }
    f = modes[mode]
    print('Converting image to brightness scale.')
    new_image = [
        [f(column) for column in row]
        for row in image
    ]
    print('Conversion Complete!')
    return np.array(new_image)
       
def invert_image(image):
    return 255 - image
       
def pixel_to_ascii(image, ascii_scale):
    """
    Maps a pixel value into an ASCII scale. For instance if the scale is "01", then pixels 0-127 will be converted to '0' and 128-255 will be converted to '1'.
    """
    range = math.ceil(255 / len(ascii_scale))
    to_ascii = np.vectorize(lambda pixel_value: ascii_scale[pixel_value // range])
    print('Converting to ASCII..')
    image = to_ascii(image)
    print('Conversion Complete!')
    return image
    
def save_as_text(image, name):
    """
    Saves the converted image into a text file.
    """
    with open(f'{name}.txt', 'w') as f:
        for x in image:
            for y in x:
                f.write(y)
            f.write('\n') 
    print(f"Saved output to {name}.txt")
        
def driver(location, mode, name, ascii_scale, invert):
    """
    Driver function that just calls all the functions.
    """
    image = load_image(location)
    image = rgb_to_brightness(image, mode)
    if invert:
        image = invert_image(image)
    image = pixel_to_ascii(image, ascii_scale)
    save_as_text(image, name)
        
if __name__ == '__main__':
    """
    If the script is run standalone, this stuff defines the argument parser and handles any errors there.
    If you're importing this script somewhere, none of this stuff will execute.
    """
    parser = argparse.ArgumentParser(description='Convert an image into ASCII.')
    parser.add_argument('location', metavar='location', help='location of the image to convert.')
    parser.add_argument('-mode', metavar='mode', help='type of rgb to brightness conversion.', default='average', choices=['average', 'luminosity', 'min_max', 'max', 'min'])
    parser.add_argument('-scale', metavar='scale', help='scale of brightness/character set to use', default="`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$")
    parser.add_argument('-name', metavar='name', help='name of the output file', default='output')
    parser.add_argument('--invert', help='invert the color scheme', action='store_true')
    args = parser.parse_args()
    location = args.location
    mode = args.mode
    name = args.name
    ascii_scale = args.scale
    invert = args.invert
    driver(location, mode, name, ascii_scale, invert)