# for n in range(5, 10_000):
#     print(n)
#     s = '1' * n + '7'
#
#     while '117' in s or '17' in s:
#         if '117' in s:
#             s = s.replace('117', '73')
#         else:
#             s = s.replace('17', '1117')
#
#     sum_digits = sum(int(x) for x in s)
#
#     if sum_digits == 22:
#         print(n)
#         break


def process_string(s):
    """
    Функция выполняет преобразования над строкой s,
    пока возможны замены '117' -> '73' или '17' -> '1117'.
    """
    while '117' in s or '17' in s:
        if '117' in s:
            s = s.replace('117', '73', 1)
        else:
            s = s.replace('17', '1117', 1)
    return s


def sum_of_digits(s):
    """
    Функция вычисляет сумму цифр в строке s.
    """
    return sum(int(char) for char in s)


# Итерация по значениям n
for n in range(4, 10001):
    # Генерация начальной строки
    s = '1' * n + '7'

    # Применение преобразований
    final_s = process_string(s)

    # Вычисление суммы цифр
    digit_sum = sum_of_digits(final_s)

    # Проверка условия
    if digit_sum == 22:
        print(n)
        break