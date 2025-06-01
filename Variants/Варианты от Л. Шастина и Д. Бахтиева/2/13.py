from ipaddress import *

net = ip_network('123.222.111.192/255.255.255.248', 0)

k = 0
for ip in net:
    new_ip = f"{ip:b}"
    if (new_ip[24:33].count('0')) % 3 != 0:
        k += 1

print(k)