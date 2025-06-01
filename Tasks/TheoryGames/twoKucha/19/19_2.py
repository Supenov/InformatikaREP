# +1 ; *2
# S1 = 14 ; S2 = s
# 1<=S<=71
# Win S >= 86

def f(s1, s2, h):
    if h == 2 and s1 + s2 >= 86:
        return 1
    elif h == 2 and s1 + s2 < 86:
        return 0
    elif s1 + s2 < 86 and h < 2:
        return 0
    else:
        if h % 2 == 1:
            return f(s1 + 1, s2, h + 1) or f(s1, s2 + 1, h + 1)\
                or f(s1 * 2, s2, h + 1) or f(s1, s2 * 2, h + 1)

        else:
            return f(s1 + 1, s2, h + 1) or f(s1, s2 + 1, h + 1)\
                or f(s1 * 2, s2, h + 1) or f(s1, s2 * 2, h + 1)


for s2 in range(1, 72):
    if f(s2, 14, 0) == 1:
        print(s2)
        break

# 15



def f(x, y, h):
    if h == 2 and x + y >= 86:
        return 1
    elif h == 2 and x + y < 86:
        return 0
    elif x + y >= 86 and h < 2:
        return 0
    else:
        if h % 2 == 1:
            return f(x + 1, y, h + 1) or f(x, y + 1, h + 1) or f(x * 2, y, h + 1) or f(x, y * 2, h + 1)  # стратегия победителя
        else:
            return f(x + 1, y, h + 1) or f(x, y + 1, h + 1) or f(x * 2, y, h + 1) or f(x, y * 2, h + 1)  # стратегия проигравшего(неудачный ход)

for x in range(1, 72):
    if f(x, 14, 0) == 1:
        print(x)
        break