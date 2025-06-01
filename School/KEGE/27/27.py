from math import dist
from turtle import *
from random import *

'''Список всех точек'''
data = []

'''Добавляем точки из файла в список'''
for s in open('27_7b.txt'): # Нужны РАЗНЫЕ файлы для пунктов А и Б
    x, y = [float(d) for d in s.split()]
    data.append([x, y])


clusters = [] # Список всех кластеров

while data: # Пока есть точки в списке
    cl = [data.pop()] # Добавляем случайную точку
    for p in cl:
        sosed = [p1 for p1 in data if dist(p, p1) < 0.1] # Ищем соседей точки ДЛЯ ФАЙЛА a < 3

        for p1 in sosed:
            cl.append(p1) # Добавляем соседа в кластер
            data.remove(p1) # Удаляем точку из списка data, чтобы не было повторений
    
    clusters.append(cl) # Добавляем получившейся кластер в список ВСЕХ кластеров

print([len(cl) for cl in clusters])


'''Проверка кластеров Черепахой'''
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
    
    return min(m)[1]



cen = [centroid(cl) for cl in clusters]
px = sum(x for x, y in cen) / len(cen)
py = sum(y for x, y in cen) / len(cen)


print(int(px*10000), int(py*10000))