import pyshark

import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--interface", required=True,
	help="Destination IP")
ap.add_argument("-f", "--filter", required=False,
	help="Spoofing IP")

args = vars(ap.parse_args())

print(args)

interface = args["interface"]
filterInfo = args["filter"]

capture = None

if filterInfo is None : 
    capture = pyshark.LiveCapture(interface=interface)
else :
    capture = pyshark.LiveCapture(interface=interface, bpf_filter=filterInfo)    

pyshark_out = open("sniffingResult.cap", "a")


for packet in capture.sniff_continuously():
    #pyshark_out.write(str(packet))
    print(packet)

