file = open('26.txt')
first_string = file.readline().split() # Разбиваем 1 строчку на split, чтобы найти S и N

S = int(first_string[0]) # Размер свободного места на диске
N = int(first_string[1]) # Количество пользователей
my_aray = [] # Массив объёма файлов

for i in range(N): # Перебираем всех пользователей
    number = int(file.readline()) # Находим объёмы файлов
    my_aray.append(number) # Добавляем объёмы в список

my_aray.sort() # Сортируем объёмы файлов ОТ МЕНЬШЕГО К БОЛЬШЕМУ
# print(my_aray)

disk = []
for i in range(len(my_aray)): # Идём слева направо
    if sum(disk) + my_aray[i] <= S: # Если объём на диске меньше объёма всех файлов S, добавляем его на Диск
        disk.append(my_aray[i]) # Добавляем объём на Диск
    else:
        break # Если места на Диске нет, выходим

disk = disk[:-1] # Удаляем последний объём на Диске, чтобы проверить возможно ли добавить больший объём

# Проверка, возможно ли добавить БОЛЬШИЙ объём на Диск
for i in range(len(my_aray) -1, -1, -1): # Идём справа налево
    if sum(disk) + my_aray[i] <= S: # Если объём на диске меньше объёма S, добавляем больший объём на Диск
        disk.append(my_aray[i]) # Добавляем больший объём на Диск
        break

print(len(disk), my_aray[-1])