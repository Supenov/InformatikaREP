from math import dist
from turtle import *
from random import *

data = []

for s in open('27_A_17916.txt'):
    x, y = [float(d) for d in s.split()]
    data.append([x, y])


clusters = []

while data:
    cl = [data.pop()]
    for p in cl:
        sosed = [p1 for p1 in data if dist(p, p1) < 0.2]

        for p1 in sosed:
            cl.append(p1)
            data.remove(p1)
    
    clusters.append(cl)


# penup() ; tracer(0)
# for cl in clusters:
#     color = random(), random(), random()
#     for x, y in cl:
#         goto(x * 20, y * 20)
#         dot(3, color)

# input()
# done()


def centroid(cl):
    m = []
    for p in cl:
        s = 0
        for p1 in cl:
            s += dist(p, p1)
        m.append([s, p])
    
    return min(m)[-1]

cen = [centroid(cl) for cl in clusters]

px = sum(x for x, y in cen) / len(cen)
py = sum(y for x, y in cen) / len(cen)

print(int(px*10000), int(py*10000))