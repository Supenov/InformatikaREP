file = open("9_5.txt")

k = 0
for i in file:
    a = sorted([int(x) for x in i.split()])

    pov2 = [x for x in a if a.count(x) == 2]

    if a[-1] < (a[0] + a[1] + a[2]):
        if len(pov2) == 2:
            k += 1
print(k)