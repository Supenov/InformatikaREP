def perevod(n, b):
    box = []

    while n > 0:
        box.append(n % b)
        n //= b

    return box

c = 0
box = []

for x in range(2031):
    s = 7**91 + 7**160 - x

    answer = perevod(s, 7)

    if str(answer).count("0") == 70:
        box.append(x)


print(max(box))