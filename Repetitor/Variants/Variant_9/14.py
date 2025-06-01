def zero_counter(n):
    string = ""
    while n > 0:
        string = str(n % 7) + string
        n //= 7

    return string.count('0')

box = []
for x in range(1, 10_000):
    num = 7 ** 270 + 7 ** 170 + 7 ** 70 - x
    if zero_counter(num) == 203:
        print(x)