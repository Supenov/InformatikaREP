print('x y z w')

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                # f1 = ( w or (not y) ) <= ( z == x )
                # if f1 == 1:
                #     print(x, y, z, w)

                f2 = ( w or (not y) ) == ( x <= z )
                if f2 == 1:
                    print(x, y, z, w)