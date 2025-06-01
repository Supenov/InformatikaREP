from functools import lru_cache

@lru_cache(None)

def f(n):
    if n < 222:
        return 111
    if n >= 222:
        return 2 * (n + 4) + f(n - 3)

for i in range(100_000):
    f(i)

print(f(55555) - f(55543))