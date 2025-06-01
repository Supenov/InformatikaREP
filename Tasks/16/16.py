def f(n):
    if n == 1:
        return 1
    if n >= 2 and n % 2 == 0:
        return f(n / 2) + 1
    if n >= 2 and n % 2 != 0: 
        return f(n - 1) + n


box = []
for n in range(1, 1001):
    g = f(n)
    if g == 19:
        box.append(n)

print(min(box))