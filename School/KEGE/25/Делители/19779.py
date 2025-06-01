import math

def is_prime(n):
    if n < 2:
        return False
    for k in range(2, int(math.isqrt(n)) + 1):
        if n % k == 0:
            return False
    return True

def f(limit=55_000_001):
    result = []
    i = limit

    while len(result) < 4:
        prime_divs = []
        for j in range(2, int(math.isqrt(i)) + 1):
            if i % j == 0:
                if is_prime(j):
                    prime_divs.append(j)
                if j != i // j and is_prime(i // j):
                    prime_divs.append(i // j)
        
        if prime_divs:

            for x in prime_divs:
                if str(x)[-3:] == '777':
                    result.append((i, x))
                    print(i, x)
        i += 1    


f()

'''55000662 9166777
55001262 2777
55001554 27500777
55001704 1777
'''