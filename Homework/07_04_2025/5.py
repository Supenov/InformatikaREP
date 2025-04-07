def f(x, y, a):
    return (x - 3*y < a) or (y > 400) or (x > 56)

for a in range(1, 201):
    if all(f(x, y, a) == 1 for x in range(1, 101) for y in range(1, 101)):
        print(a) ; break