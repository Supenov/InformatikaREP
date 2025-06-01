import math

def is_prime(n):
    if n < 2:
        return False
    for k in range(2, int(math.isqrt(n)) + 1):
        if n % k == 0:
            return False
    return True


def f(limit=55_000_001, max_count=4):
    results = []
    i = limit
    while len(results) < max_count:
        prime_divs = []
        for j in range(2, int(math.isqrt(i)) + 1):
            if i % j == 0:
                if is_prime(j):
                    prime_divs.append(j)
                if j != i // j and is_prime(i // j):
                    prime_divs.append(i // j)
        if prime_divs:

            F = sum(prime_divs) // len(prime_divs)
            if F != 0 and F % 813 == 0:
                results.append((i, F))
                print(i, F)
        i += 1
f()