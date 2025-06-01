def f(x, a):
    return ( (x % 7 != 0) and (x % 13 == 0) ) <= (x > a - 40)

for A in range(1, 10000):
    if all(f(x, A) == 1 for x in range(1, 10000)):
        print(A)