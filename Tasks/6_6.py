from turtle import *
screensize(2000, 2000)
tracer(1)
left(90)
size = 45

pendown()

for i in range(3):
    forward(2 * size)
    right(90)
    forward(3 * size)
    left(90)

right(180)
forward(6 * size)
right(90)
forward(9 * size)

penup()

backward(3 * size)
right(90)

pendown()

for i in range(2):
    forward(1 * size)
    right(90)
    forward(2 * size)
    left(90)

right(180)
forward(3 * size)
right(90)
forward(4 * size)
right(90)
forward(1 * size)

penup()

for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * size, y * size)
        dot(6, "red")

input()
done()

# 12