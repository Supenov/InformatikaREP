clustersB = [[], [], []]

for i in open('27_B_21425 (1).txt'):
    x, y = [float(j) for j in i.split()]
    if x < 0:
        clustersB[0].append([x, y])
    elif x < 22:
        clustersB[1].append([x, y])
    else:
        clustersB[2].append([x, y])


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def center(cl):
    m = []
    for p in cl:
        sm = sum(dist(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]


centerB = [center(cl) for cl in clustersB]

px = sum(x for x, y in centerB) / 3 * 10000
py = sum(y for x, y in centerB) / 3 * 10000
print(int(px), int(py))
