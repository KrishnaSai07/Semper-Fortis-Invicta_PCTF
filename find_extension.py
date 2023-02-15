import argparse
import magic

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--filename", required=True,
	help="Filename")
 

args = vars(ap.parse_args())

temp = magic.from_file(args["filename"])

print(temp)

