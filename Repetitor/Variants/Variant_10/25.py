from fnmatch import fnmatch


def product_of_digits(number):
    # Преобразуем число в строку
    number_str = str(number)

    # Инициализируем произведение
    product = 1

    # Проходим по каждой цифре
    for digit in number_str:
        # Преобразуем символ цифры обратно в число и умножаем
        product *= int(digit)

    return product


for x in range(4321, 10**9, 4321):
    if fnmatch(str(x), '34*56?7'):
        print(x, product_of_digits(x))


