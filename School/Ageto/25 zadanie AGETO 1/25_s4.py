def f(n):
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return n // d + d
    return 0

count = 0
for i in range(700_001, 700_001 + 100_000):
    k = f(i)

    if k % 10 == 4:
        print(i, k)
        count += 1
    if count == 5:
        break


"""
700004 350004
700009 41194
700023 233344
700024 350014
700044 350024
"""