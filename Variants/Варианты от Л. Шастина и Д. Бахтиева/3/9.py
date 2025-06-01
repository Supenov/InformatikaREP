file = open('9.txt')

k = 0
for i in file:
    a = sorted(int(x) for x in i.split())

    pov2 = [x for x in a if a.count(x) == 2]
    nepov = [x for x in a if a.count(x) == 1]

    negative = [x for x in a if x < 0]
    positive = [x for x in a if x > 0]

    if (len(pov2) == 2) and (len(nepov) == 4) and ( abs(sum(negative)) > sum(positive) ):
        k += 1

print(k)