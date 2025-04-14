from turtle import *
screensize(2000, 2000)
tracer(0)
size = 75
left(90)
pendown()

right(30)
for i in range(3):
    right(150)
    forward(6 * size)
    right(30)
    forward(12 * size)

penup()

for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * size, y * size)
        dot(8, "red")

input()
done()