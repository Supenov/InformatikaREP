with open("9_3.txt") as file:
    for i in file:
        a = sorted([int(x) for x in i.split()])

        pov2 = [x for x in a if a.count(x) == 2]
        nepov = [x for x in a if a.count(x) == 1]

        mx = a[-1]
        mn = a[0]
        middle = a[1:-1]

        if len(pov2) == 4 and len(nepov) == 2:
            if mx in nepov:
                if (mx * mn) > sum(middle):
                    print(a, sum(a))
                    break