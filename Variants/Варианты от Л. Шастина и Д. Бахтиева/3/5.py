def converter(num):
    string = ''
    while num > 0:
        string = str(num % 3) + string
        num //= 3
    return string


box = []
for n in range(1, 10_000):
    new_n = converter(n)
    sum_nums = sum(int(x) for x in new_n)

    if sum_nums % 2 == 0:
        new_n = '1' + new_n + '2'
    else:
        new_n = '2' + new_n + '0'

    R = int(new_n, 3)

    if R > 100:
        box.append(R)

print(min(box))