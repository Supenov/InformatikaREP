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
n = 550_001

while count < 6:
    # Находим наибольший делитель числа n
    max_div = f(n)
    
    # Проверяем, является ли наибольший делитель составным (не простым)
    if max_div > 1 and not is_prime(max_div):
        print(n, max_div)
        count += 1
    
    n += 1


"""
550002 275001
550004 275002
550005 183335
550008 275004
550010 275005
550011 183337
"""