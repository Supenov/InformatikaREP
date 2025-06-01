file = open("9_7.txt")

k = 0
for i in file:
    k += 1
    a = sorted([int(x) for x in i.split()])

    pov3 = [x for x in a if a.count(x) == 3]
    nepov = [x for x in a if a.count(x) == 1]

    if len(pov3) == 6 and len(nepov) == 1:
        if (sum(pov3) / len(pov3)) < nepov[0]:
            print(k, a)