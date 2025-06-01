import math

def is_prime(n):
    if n < 2:
        return False
    for k in range(2, int(math.isqrt(n)) + 1):
        if n % k == 0:
            return False
    return True


def f(limit=32_500_001):
    result = []
    i = limit

    while len(result) < 7:
        prime_div = []

        for j in range(2, int(math.isqrt(i)) + 1):
            if i % j == 0:
                if is_prime(j):
                    prime_div.append(j)
                if j != i // j and is_prime(i // j):
                    prime_div.append(i // j)
        

        if prime_div:
            prime_div = sorted(set(prime_div))
            S = sum(prime_div)
        else:
            S = 0
        
        if S != 0 and S % 145 == 0:
            result.append((i, S))
            print(i, S)
        
        i += 1

f()