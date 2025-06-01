from ipaddress import *

net = ip_network("172.16.168.0/255.255.248.0")
c = 0

for ip in net:
    new_ip = f"{ip:b}"
    if new_ip.count("1") % 5 != 0:
        c += 1

print(c)
# 1663