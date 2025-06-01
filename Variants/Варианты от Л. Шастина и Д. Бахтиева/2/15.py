def f(x, a1, a2):
    M = 32 <= x <= 68
    N = 54 <= x <= 76
    A = a1 <= x <= a2

    return not( (M or N ) == (not(A)) )


for a1 in range(30, 78):
    for a2 in range(a1+1, 78):
        if all(f(x, a1, a2) == 1 for x in range(1, 1000)):
            print(a2-a1)