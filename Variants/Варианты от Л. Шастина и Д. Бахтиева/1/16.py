from functools import lru_cache

@lru_cache(None)

def f(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 == 0:
        return f(n - 1) + n - 1
    if n > 2 and n % 2 != 0:
        return f(n - 2) + 2 * n - 2
    return False

for i in range(4000):
    f(i)

print(f(3048) - f(3045))