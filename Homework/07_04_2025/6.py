b = set(range(170, 221))

def f(x, a):
    B = x in b
    
    return (x % a == 0) or (B <= (x % 24 != 0))

c = 0
for A in range(1, 201):
    if all(f(x, A) == 1 for x in range(1, 101)):
        c += 1
print(c)


