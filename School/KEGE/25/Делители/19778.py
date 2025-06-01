# import math

# def f(limit=9_500_001, counter=0):
#     divs = []
#     for i in range(limit, limit+1_000_000):
#         for j in range(2, int(math.isqrt(i) + 1)):
#             if i % j == 0:
#                 divs.append(j)
#                 if j != i // j:
#                     divs.append(i // j)
#     if len(divs) > 0:
#         F = sum(divs)
#     else:
#         F = 0
    
#     if F != 0 and F % 813 == 0:
#         counter += 1
#         print(i, F)
        
# f()


import math

def is_prime(n):
    """Проверяет, является ли число n простым."""
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_special_numbers(limit=9_500_001, max_count=5):
    results = []
    i = limit
    while len(results) < max_count:
        prime_divisors = []
        for j in range(2, int(math.isqrt(i)) + 1):
            if i % j == 0:
                if is_prime(j):  # Проверяем, является ли делитель простым
                    prime_divisors.append(j)
                if j != i // j and is_prime(i // j):  # Проверяем парный делитель
                    prime_divisors.append(i // j)
        
        if prime_divisors:
            # Вычисляем целую часть среднего арифметического простых делителей
            F = sum(prime_divisors) // len(prime_divisors)
            if F != 0 and F % 813 == 0:
                results.append((i, F))
                print(f"N = {i}, F = {F}")
        
        i += 1

# Запуск функции
find_special_numbers()