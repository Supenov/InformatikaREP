from turtle import *
screensize(2000, 2000)
tracer(0)
left(90)
size = 30

pendown()

for i in range(3):
    forward(11 * size)
    right(90)
    forward(24 * size)
    right(90)

penup()

forward(2 * size)
right(90)
forward(5 * size)
left(90)

pendown()

for i in range(3):
    forward(6 * size)
    left(90)
    forward(9 * size)
    left(90)

penup()

for x in range(-20, 40):
    for y in range(-20, 20):
        setpos(x * size, y * size)
        dot(5, "red")

input()
done()

# a1 = 25, b1 = 12 <=> 300 точек
# a2 = 10, b2 = 7 <=> 70 точек
# 370 - 42 == 328 точек

# ОТВЕТ: 328