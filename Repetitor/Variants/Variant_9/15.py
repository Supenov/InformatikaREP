def f(A, x):
    return (A + 2*x > 400 - A) and (A % 100 + 120 % A > 140)


for A in range(1, 2000):
    if all(f(A, x) == 1 for x in range(1, 100000)):
        print(A)
        break