for i in range(10_000_001, 10_100_001):
    divs = []
    for j in range(2, i):
        if i % j == 0:
            divs.append(j)
    
    if len(divs) < 2:
        m = 0
    else:
        m = divs[-1] + divs[-2]
    
    if 0 < m < 10_000:
        print(m, i)

# 6976 6374 6924 8024 8358


# import math


# def find_special_numbers(limit=10_000_001, max_m=10_000, counter=0):
    
#     for i in range(limit, limit + 1_000_000):  # Ограничиваем диапазон для тестирования
#         divs = []
#         for j in range(2, int(math.isqrt(i)) + 1):
#             if i % j == 0:
#                 divs.append(j)
#                 if j != i // j:  # Добавляем парный делитель, если он отличается
#                     divs.append(i // j)
        
#         if len(divs) < 2:
#             m = 0
#         else:
#             divs.sort()  # Сортируем делители
#             m = divs[-1] + divs[-2]
        
#         if 0 < m < max_m:
#             counter += 1
#             print(m, i)
#             if counter == 5:
#                 break

# # Запуск функции
# find_special_numbers()

'''
6876 10000043       
6374 10000153
6924 10000163
8024 10000183
8358 10000217
'''