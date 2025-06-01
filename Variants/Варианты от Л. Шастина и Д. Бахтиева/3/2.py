print('a b c d')

for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            for d in 0, 1:
                F = ( (a <= b) == c ) or d
                if F == 0:
                    print(a, b, c, d)

# a d b c