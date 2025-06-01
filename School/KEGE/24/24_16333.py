

# Чтение данных из файла
with open('24_16333.txt') as f:
    s = f.readline().strip()

# Функция для проверки, является ли символ буквой
def is_letter(c):
    return c.isalpha()

# Поиск максимальной последовательности
max_length = 0
current_length = 1  # Текущая длина последовательности

for i in range(1, len(s)):
    # Если текущий и предыдущий символы не нарушают чередование
    if is_letter(s[i]) != is_letter(s[i - 1]):
        current_length += 1
    else:
        max_length = max(max_length, current_length)
        current_length = 1  # Сброс длины при нарушении чередования

# Проверка последней последовательности
max_length = max(max_length, current_length)

print(max_length)