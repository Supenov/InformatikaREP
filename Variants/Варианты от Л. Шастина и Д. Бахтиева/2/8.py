from itertools import *

k = 0
for x in product(sorted('ЛЮСТРА'), repeat=5):
    s = ''.join(x)

    if (s.count('Ю') <= 2) and (s[-1] not in 'ЛСТР'):
        k += 1

print(k)