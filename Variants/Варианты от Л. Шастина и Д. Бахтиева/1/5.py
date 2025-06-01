box = []


def perevod(n):
    string = ''
    while n > 0:
        string = str(n % 8) + string
        n = n // 8
    return string


for n in range(1, 10_000):
    b = perevod(n)

    sum_digits = sum(int(x) for x in b)
    if sum_digits % 2 == 0:
        b += str(perevod(sum_digits))
    else:
        b = str(perevod(sum_digits)) + b

    R = int(b, 8)



    if n > 482:
        print(n, R)
        box.append(R)

print(min(box))
