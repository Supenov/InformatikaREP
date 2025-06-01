from turtle import *
screensize(2000, 2000)
tracer(0)
left(90)
size = 20

pendown()

for i in range(9):
    forward(27 * size)
    right(90)
    forward(30 * size)
    right(90)

penup()

forward(3 * size)
right(90)
forward(6 * size)
left(90)

pendown()

for i in range(9):
    forward(77 * size)
    right(90)
    forward(66 * size)
    right(90)

penup()

for x in range(-20, 35):
    for y in range(-20, 35):
        setpos(x * size, y * size)
        dot(4, "red")

input()
done()

# 94