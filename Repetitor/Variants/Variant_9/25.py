c = 0

def is_prime(n):
    if n < 2:
        return False
    for k in range(2, int(n**0.5) + 1):
        if n % k == 0:
            return False
    return True


for i in range(3_333_337+1, 10**40):
    d = []
    for j in range(1, i):
        if i % j == 0:
            if is_prime(j):
                d.append(j)

    R = d[-1] - d[0]

    if R > 1000 and R % 3 == 0:
        print(i, R)
        c += 1
        if c == 5:
            break

