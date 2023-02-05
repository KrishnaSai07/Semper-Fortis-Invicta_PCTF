import sys
import socket
import time
import subprocess
from collections import defaultdict

# Dictionary to store IP addresses and request count
ip_requests = defaultdict(int)

# Threshold value to determine if an IP is a part of a DDoS attack
THRESHOLD = 1000

# Time window to consider when calculating request rate
WINDOW = 60

# List to store banned IPs
banned_ips = []

# Function to calculate request rate for an IP address
def calculate_request_rate(ip):
    current_time = time.time()
    request_count = 0
    for timestamp, src_ip in ip_requests[ip]:
        if current_time - timestamp < WINDOW:
            request_count += 1
    return request_count / WINDOW


for line in sys.stdin:
    ip = line.strip().split(" ")[0]
   
    ip_requests[ip].append((time.time(), ip))

    request_rate = calculate_request_rate(ip)
    if request_rate > THRESHOLD:
        # Adding IP to banned list
        banned_ips.append(ip)

        # Blocking IP by adding it to firewall rule
        # (Assuming iptables is used in PCTF Server/ VM Machine)
        # Need to replace the below rule with appropriate command as per server
        subprocess.call(["iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"])

# Periodically checking for banned IPs to unban
while True:
    for ip in banned_ips:
        request_rate = calculate_request_rate(ip)
        if request_rate < THRESHOLD:
            banned_ips.remove(ip)
            # Unblocking IP by removing it from firewall rule
            subprocess.call(["iptables", "-D", "INPUT", "-s", ip, "-j", "DROP"])
    time.sleep(WINDOW)

