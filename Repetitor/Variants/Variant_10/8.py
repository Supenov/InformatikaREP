from itertools import product, repeat

trigger_1 = 'МАСИК'
trigger_2 = 'ЧЕЧИК'

k = 0
c = 0
for x in product(sorted('ЧМСЕИАК'), repeat=5):

    k += 1
    s = ''.join(x)

    if s != trigger_1:
        continue
    else:
        c += 1

    if s != trigger_2:
        continue
    else:
        print(c)
        break
