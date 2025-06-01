file_A = open('27_A_21932.txt')
file_B = open('27_B_21932.txt')

clustersA = [[], []]

for i in file_A:
    x, y = [float(j) for j in i.split()]
    if y > 10:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def center(cl):
    m = []
    for p in cl:
        sm = sum(dist(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]


centersA = [center(cl) for cl in clustersA]

# for i in clustersA:
#     print(len(i))

print(int(centersA[0][0]*10000), int(centersA[1][1]*10000))


clustersB = [[], [], []]

for k in file_B:
    x, y = [float(m) for m in k.split()]
    if y < 10:
        clustersB[0].append([x, y])
    elif x < 17:
        clustersB[1].append([x, y])
    else:
        clustersB[2].append([x, y])

centersB = [center(cl) for cl in clustersB]

# for i in clustersB:
#     print(len(i))

print(int(centersB[1][0] * 10000), int(centersB[0][1] * 10000))

# print(int(pxB), int(pyB))