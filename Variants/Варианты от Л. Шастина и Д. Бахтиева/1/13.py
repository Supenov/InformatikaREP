from ipaddress import *

net = ip_network('172.16.160.0/255.255.240.0')

k = 0
for ip in net:
    ip1 = f"{ip:b}"
    if ip1.count('1') % 4 != 0:
        k += 1
        print(ip)

print(k - 2)

