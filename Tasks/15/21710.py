def f(x, a1, a2):
    B = 36 <= x <= 75
    C = 60 <= x <= 110
    A = a1 <= x <= a2

    return (not A) <= (B == C)

for a1 in range(35, 111):
    for a2 in range(a1+1, 112):
        if all(f(x, a1, a2) == 1 for x in range(30, 115)):
            print(a2-a1)