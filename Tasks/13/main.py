from ipaddress import *

# net = ip_network("162.198.0.157/255.255.255.224", 0)
# k = 0
#
# for ip in net:
#     print(ip, k)
#     k += 1

# k = 0
# net = ip_network("192.168.32.160/255.255.255.240")
#
# for ip in net:
#     new_ip = f"{ip:b}"
#     if new_ip.count('1') % 2 == 0:
#         k += 1
#
# print(k)


# for mask in range(32, 1, -1):
#     net1 = ip_network(f"114.91.57.39/{mask}", 0)
#     net2 = ip_network(f"114.91.19.61/{mask}", 0)
#
#     if net1 == net2:
#         k = 0
#         for ip in net1:
#             new_ip = f"{ip:b}"
#             if new_ip.count('1') % 2 == 0:
#                 k += 1
#
#         print(k)


# for mask in range(32, 10, -1):
#     k = 0
#     net1 = ip_network(f"147.222.199.75/{mask}", 0)
#     for i in net1:
#         new_i = f"{i:b}"
#         if (new_i[:8] == new_i[-8:]) and (new_i[8:16] == new_i[-16:-8]):
#             k += 1
#             print(i)
#     if k != 0:
#         print(mask)