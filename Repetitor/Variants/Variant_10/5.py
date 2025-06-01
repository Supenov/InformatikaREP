def convert_base(number):
    string = ""

    while number > 0:
        string = str(number % 3) + string
        number = number // 3
    return string

def sum_numbers(string):
    return sum(int(x) for x in string)

box = []
for n in range(5, 10_000):
    tri_n = convert_base(n)

    l1 = tri_n[-1]
    l2 = tri_n[-2]


    if n % 3 == 0:
        tri_n = l2 + l1 + tri_n
    else:
        tri_n = convert_base(sum_numbers(tri_n)) + tri_n

    R = int(tri_n, 3)

    if R > 418 and R % 2 != 0:
        box.append(R)

print(min(box))
