from turtle import *
screensize(2000, 2000)
tracer(0)
left(90)
size = 30
pendown()


for i in range(14):
    right(60)
    forward(2 * size)
    right(60)
    forward(2 * size)
    right(270)

penup()

for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * size, y * size)
        dot(4, "red")

input()
done()

# 148