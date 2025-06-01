def f(n):
    d = []
    while n > 0:
        d.append(n % 7)
        n = n // 7
    return d.count(0)    


box = []
#max_zero = -100

for x in range(1, 2031):
    s = 7**170 + 7**100 - x
    if f(s) == 73:
        box.append(x)
    #count_zero = f(s)
    #max_zero = max(count_zero, max_zero) = 73

print(max(box))
#print(max_zero) = 73