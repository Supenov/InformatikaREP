file = open("9_6.txt")

k = 0
for i in file:
    k += 1
    a = sorted([int(x) for x in i.split()], reverse=True)

    b = a.copy()

    mx = b.pop(0)
    mn = b.pop()

    if ((mx + mn) // 2) > (sum(b) / len(b)):
        print(k, a, sum(a), sum(b), len(b))
        break
