import math

def is_prime(n):
    if n < 2:
        return False
    for k in range(2, int(math.isqrt(n)) + 1):
        if n % k == 0:
            return False
    return True


def f(limit=23_600_001):
    result = []
    i = limit

    while len(result) < 6:
        prime_div = []

        for j in range(2, int(math.isqrt(i)) + 1):
            if i % j == 0:
                if is_prime(j):
                    prime_div.append(j)
                if j != i // j and is_prime(i // j):
                    prime_div.append(i // j)
        

        if prime_div:
            prime_div = sorted(set(prime_div))
            M = prime_div[0] + prime_div[-1]
        else:
            M = 0
        
        if M % 213 == 171:
            result.append((i, M))
            print(i, M)

        i += 1

f()


'''
23600182 694125
23600442 28713
23600478 357585
23600570 1449
23600838 135639
23600970 29139
'''