# img2ascii

![example](https://raw.githubusercontent.com/akashsara/img2ascii/master/output/cover.jpg)

---

## What is it?

It converts an [image](https://github.com/akashsara/img2ascii/blob/master/output/test.jpg) into a text file containing an equivalent ASCII [image](https://raw.githubusercontent.com/akashsara/img2ascii/master/output/luminosity.txt). (If the text file looks like gibberish, zoom out as much as you can). The code is modular and can easily be modified. You can also include this in your own packages by adding this file in and importing it. I've commented it enough that everything should make sense, but open up an issue if you have trouble understanding it.

> image is from [Unsplash](https://unsplash.com/). It's a website that hosts a ton of free to use images. 100% totally free. The particular [image](https://unsplash.com/photos/lOYyakxnMu0) I used is by Zdeněk Macháček.

## Installation

1. Download & install [Python3](https://www.python.org/downloads/).
2. Clone or download this repository.
3. Navigate to this repository and run `pip install -r requirements.txt`
4. Run the script: `python img2ascii.py LOCATION`

## Usage

`
img2ascii.py location
			 [-h] [-mode MODE] [-scale SCALE] [-name NAME] 
			 [--invert]
`

#### Required Arguments:

`location` - Specify the path to the image to convert. This can be an absolute path or a path relative to the directory the script is running on.

#### Optional Arguments:

`h`: Just displays the help menu which details most of the information here.

`mode MODE`: Conversion mode. Determines which method to use to convert each RGB pixel into a single brightness value. See [working](#what-does-it-actually-do) for more information. Must be one of `average`, `luminosity`, `min_max`, `max`, `min`. Default: `average`

`scale SCALE`: Brightness scale. Determines the character set to replace each pixel with. Default: ```"`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"```

`name NAME`: Output file name. Specifies the name of the file the output is saved in. Default: `output`.

`invert`: Invert flag. Inverts the brightness scale. So 0 would become 255 and 255 would become 0. Default: `False`.

## Can I use this in my own scripts/packages/software?

Yup. Feel free to do anything with this script. Be sure to credit me/this repo though. And if you make something cool, do share it. :)

## What does it actually do?

1. Take in an RGB image. Each pixel is represented as a tuple (R, G, B).
2. For each pixel, squash the values of R, G and B into a single value, brightness.
3. Map this brightness value onto the brightness scale (list of ASCII characters we're replacing the pixels with).
4. Do the above two steps for every pixel in the image.
5. Write it to a file.
6. Voila!


## Okay, but why? 

Not a clue. Seemed fun at the time. And some of the outputs are funny.