from scapy.all import *
import time 
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-di", "--destination-ip", required=True,
	help="Destination IP")
ap.add_argument("-si", "--spoofing-ip", required=True,
	help="Spoofing IP")
ap.add_argument("-sp", "--source-port", required=True,
	help="source port")
ap.add_argument("-dp", "--destination-port", required=True,
	help="destination port")
ap.add_argument("-hip", "--host-ip", required=False,
	help="Host IP")				

args = vars(ap.parse_args())

print(args)

destinationIp = args["destination_ip"]
spoofingIp = args["spoofing_ip"]
sourcePort = args["source_port"]
destinationPort = args["destination_port"]
hostIp = args["host_ip"]


ip = IP(src=spoofingIp,dst=destinationIp)
udp = UDP(sport = sourcePort,dport=destinationPort)

if hostIp is None:
    while(True):
        packet = ip/udp/Raw(load="Raw Packets")
        send(packet)
        time.sleep(4)

else :
    packet = ip/udp/Raw(load=hostIp)
    send(packet)

    
        
#send(packet)

#send(packet)

#while(True):
    #p = send(packet,return_packets = True)
    #print(p.show())
    #send(packet)
    #time.sleep(4)
