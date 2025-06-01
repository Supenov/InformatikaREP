file = open('19481.txt')
k = 0
box = []

for s in file:
    k += 1
    a = sorted([int(x) for x in s.split()])
    b = a.copy()

    nepov = [x for x in a if a.count(x) == 1]

    if len(nepov) == 4:
        if ( a[0]**2 + 2*a[0]*a[-1] + a[-1]**2 ) > (a[1]**3 + a[2]**3):
            box.append(k)

print(sum(box))

