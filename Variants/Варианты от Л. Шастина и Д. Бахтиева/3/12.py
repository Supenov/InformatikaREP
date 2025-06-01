box = []

for n in range(3, 10_000):
    s = '4' + '1' * n

    while '411' in s or '1111' in s:
        if '411' in s:
            s = s.replace('411', '14', 1)
        if '1111' in s:
            s = s.replace('1111', '1', 1)


    sum_numbers = sum(int(x) for x in s)
    box.append(sum_numbers)

print(max(box))