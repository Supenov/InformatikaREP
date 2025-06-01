k = 0
for i in range(1000, 10_000):
    d = []
    for j in range(1, i+1):
        if i % j == 0:
            d.append(j)

    S = sum(d)
    if str(S)[-2] + str(S)[-1] == '23':
        k += 1
        print(i, S)