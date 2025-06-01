file = open('4983.txt')
k = 0

for s in file:
    a = sorted([int(x) for x in s.split()])
    if (a[0] + a[-1])**2 > a[1]**2 + a[2]**2 + a[3]**2:
        k += 1

print(k)