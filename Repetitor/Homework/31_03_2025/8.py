from itertools import*

k = 0
for x in product(sorted('ABCX'), repeat=5):
    s = ''.join(x)
    
    if s.count('X') == 1:
        k += 1
print(k)

# 405