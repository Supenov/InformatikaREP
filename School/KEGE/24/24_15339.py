with open('24_15339.txt') as file:
    s = file.readline()

def is_letter(n):
    return n.isalpha()

m = 0
c = 0

for r in range(1, len(s)):
    if is_letter(s[r - 1]) != is_letter(s[r]):
        c += 1
    
    else:
        m = max(m, c)
        c = 1


print(m)




# # Чтение данных из файла
# with open('24_15339.txt') as f:
#     s = f.readline().strip()

# # Функция для проверки, является ли символ буквой
# def is_letter(c):
#     return c.isalpha()

# # Поиск максимальной последовательности
# max_length = 0
# current_length = 1  # Текущая длина последовательности

# for i in range(1, len(s)):
#     # Если текущий и предыдущий символы не нарушают чередование
#     if is_letter(s[i]) != is_letter(s[i - 1]):
#         current_length += 1
#     else:
#         max_length = max(max_length, current_length)
#         current_length = 1  # Сброс длины при нарушении чередования

# # Проверка последней последовательности
# max_length = max(max_length, current_length)

# print(max_length)