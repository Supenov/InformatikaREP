from itertools import *


box = []
k = 0
for x in product(sorted("СИНЕРГЯ"), repeat=6):
    k += 1
    s = "".join(x)

    if "ГИРЯ" in s:
        box.append(k)

print(max(box))