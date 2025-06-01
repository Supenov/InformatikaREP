for x in range(1, 2006):
    n = 4 ** 163 * 5 + 12 ** 62 - x

    one_counter = 0
    four_counter = 0

    while n > 0:
        if n % 5 == 1:
            one_counter += 1
        if n % 5 == 4:
            four_counter += 1

        
        n = n // 5

    if one_counter < four_counter:
        print(x)