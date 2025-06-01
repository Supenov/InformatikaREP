def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def f(n):
    max_div = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            max_div = max(max_div, i)
            if n // i != n:
                max_div = max(max_div, n // i)
    return max_div

# Счетчик найденных чисел
count = 0
# Начинаем перебор с 550 001
n = 350_001
while count < 6:
    max_div = f(n)

    if max_div > 1 and not is_prime(max_div):
        print(n, max_div)
        count += 1
    n += 1


"""
350001 116667
350002 175001
350004 175002
350007 116669
350008 175004
350009 31819
"""