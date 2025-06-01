from itertools import *

c = 0
k = 0
for x in product(sorted('ПРЕСТОЛ'), repeat=5):
    k += 1
    s = ''.join(x)

    if k % 2 != 0:
        if s[-1] in 'ЕО':
            if s.count('П') + s.count('Р') + s.count('С') + s.count('Т') + s.count('Л') <= 3:
                c += 1

print(c)