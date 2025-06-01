from itertools import *

k = 0
for x in product(sorted('БЛОГЕР'), repeat = 4):
    s = ''.join(x)

    if (s.count('Г') == 1) and ('ОЕ' not in s) and  ('ЕО' not in s):
        k += 1

print(k)