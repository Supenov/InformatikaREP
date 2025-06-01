print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ( (not x) <= z ) and (w or  (not y) ) and (not z)
                if F == 1:
                    print(x, y, z, w)