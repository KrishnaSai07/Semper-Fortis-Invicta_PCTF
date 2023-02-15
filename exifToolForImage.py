from PIL import Image
from PIL.ExifTags import TAGS

import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--filename", required=True,
	help="Filename")

args = vars(ap.parse_args())

# open the image
image = Image.open(args["filename"])

# extracting the exif metadata
exifdata = image.getexif()

# looping through all the tags present in exifdata
for tagid in exifdata:
	
	# getting the tag name instead of tag id
	tagname = TAGS.get(tagid, tagid)

	# passing the tagid to get its respective value
	value = exifdata.get(tagid)

	# printing the final result
	print(f"{tagname:25}: {value}")

