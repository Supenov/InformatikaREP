counter = 0

def is_prime(n):
    if n < 2:
        return False
    for k in range(2, n):
        if n % k == 0:
            return False
    return True

for i in range(550_001, 10**40):
    d = []

    for j in range(2, i):
        if i % j == 0:
            d.append(j)

    if d:
        mx_d = max(d)
        if mx_d != i and not(is_prime(mx_d)):
            print(i, mx_d)
            counter += 1
    if counter == 6:
        break

'''
550002 275001
550004 275002
550005 183335
550008 275004
550010 275005
550011 183337
'''


# counter = 0
# i = 550_001
#
# while counter < 6:
#     for j in range(i // 2, 0, -1):
#         if i % j == 0:
#             for k in range(2, int(j ** 0.5) + 1):
#                 if j % k == 0:
#                     print(i, j)
#                     counter += 1
#                     break
#             break
#     i += 1


# counter = 0
#
# for i in range(550_001, 10**6):
#     d = []
#     for j in range(2, int(i**0.5) + 1):
#         if i % j == 0:
#             d.append(j)
#             if j != i // j:
#                 d.append(i // j)
#
#     if d:
#         d.sort()
#         mx_d = d[-1]
#         is_prime = True
#         for k in range(2, mx_d):
#             if mx_d % k == 0:
#                 is_prime = False
#                 break
#
#         if not is_prime:
#             print(i, mx_d)
#             counter += 1
#
#     if counter == 6:
#         break