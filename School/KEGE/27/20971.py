# Import
from math import dist
from turtle import *
from random import random

# Files
file_a = open('27A_20971.txt')
file_b = open('27B_20971.txt')


data = []

for s in file_b: #file_a:
    x, y = [float(d) for d in s.split()]
    data.append([x, y])

clusters = []

while data:
    cl = [data.pop()]
    for p in cl:
        sosed = [p1 for p1 in data if dist(p, p1) < 2]
        
        for p1 in sosed:
            cl.append(p1)
            data.remove(p1)
    clusters.append(cl)


print([len(cl) for cl in clusters])


def centroid(cl):
    m = []
    for p in cl:
        s = 0
        for p1 in cl:
            s += dist(p, p1)
        m.append([s, p])
    return min(m)[1]

cen = [centroid(cl) for cl in clusters]

px = sum(x for x, y in cen) / len(cen)
py = sum(y for x, y in cen) / len(cen)

print(int(px * 10000), int(py * 10000))

# A = 54389 34006
# B = 70214 115435