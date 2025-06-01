for i in range(1_500_001, 10**40):
    divs = []
    for j in range(2, i):
        if i % j == 0:
            divs.append(j)

    if len(divs) > 0:
        R = sum(divs)
    else:
        R = 0

    if  (i % 1 == 0) and (i // R == 1):
        print(i, R)