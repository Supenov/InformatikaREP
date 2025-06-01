# s = open('24_19887.txt').readline()

# for x in '13579':
#     s = s.replace(x, 'a')
# for y in '02468':
#     s = s.replace(y, 'b')

# #print(s[:100])

# while 'ab' in s:
#     s = s.replace('ab', '*')

# s = s.replace('a', ' ').replace('b', ' ')

# print( max(len(c) for c in s.split() ) )

# Чтение данных из файла
s = open('24_19887.txt').readline()

# Замена чётных и нечётных цифр на символы 'a' и 'b'
for x in '13579':  # Нечётные цифры
    s = s.replace(x, 'a')
for y in '02468':  # Чётные цифры
    s = s.replace(y, 'b')

# Поиск самой длинной чередующейся последовательности
max_len = 0
current_len = 1  # Текущая длина чередования

for i in range(1, len(s)):
    if s[i] != s[i - 1]:  # Если текущий символ отличается от предыдущего
        current_len += 1
    else:  # Если символы совпадают, завершаем текущее чередование
        max_len = max(max_len, current_len)
        current_len = 1

# Проверяем последнюю последовательность
max_len = max(max_len, current_len)

print(max_len)