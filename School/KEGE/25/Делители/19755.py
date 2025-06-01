import math

def is_prime(n):
    if n < 2:
        return False
    for k in range(2, int(math.isqrt(n)) + 1):
        if n % k == 0:
            return False
    return True

def f(limit=1_200_000):
    result = []
    i = limit

    while len(result) < 5:
        prime_divs = []

        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                if is_prime(j):
                    prime_divs.append(j)
                if j != i // j and is_prime(i // j):
                        prime_divs.append(i // j)
        
        if prime_divs:
            prime_divs = sorted(set(prime_divs))
            M = prime_divs[0] + prime_divs[-1]
        else:
            M = 0
        
        if M > 2000 and str(M)[-1] == '8':
            result.append((i, M))
            print(i, M)
        
        i += 1

f()