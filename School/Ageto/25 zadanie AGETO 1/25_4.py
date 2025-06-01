def f(n):
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return n // d - d
    return 0

c = 0
for i in range(860_001, 860_001 + 100_000):
    k = f(i)

    if k % 100 == 18:
        c += 1
        print(i, k)
    if c == 5:
        break


"""
860040 430018
860163 286718
860219 27718
860240 430118
860440 430218
"""