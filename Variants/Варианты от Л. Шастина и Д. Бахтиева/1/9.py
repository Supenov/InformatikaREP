file = open('9.txt')
k = 0

for s in file:
    a = sorted([int(x) for x in s.split()])


    a3 = [x for x in a if a.count(x) == 2]
    a1 = [x for x in a if x not in a3]

    if (a1[0] != max(a)) and (a1[0] != min(a)) and len(a3) == 6:
        k += 1

print(k)



