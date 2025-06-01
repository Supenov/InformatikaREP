from turtle import *

tracer(0)
left(90)
screensize(5000, 5000)
pendown()

size = 45


for i in range(2):
    fd(11*size)
    rt(90)
    fd(17*size)
    rt(90)

penup()

fd(7*size)
lt(90)
bk(1*size)
rt(90)

pendown()

for i in range(2):
    fd(15*size)
    rt(90)
    fd(7 * size)
    rt(90)

penup()
for x in range(-20, 20):
    for y in range(-20, 40):
        setpos(x * size, y * size)
        dot(6, "red")

done()

# 40