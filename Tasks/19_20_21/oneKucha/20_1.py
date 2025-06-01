def f(x, h):
    if h == 3 and x >= 68:
        return 1
    elif h == 3 and x < 68:
        return 0
    elif x >= 68 and h < 3:
        return 0
    else:
        if h % 2 != 1:
            return f(x + 1, h + 1) or f(x + 4, h + 1) or f(x * 5, h + 1)
        else:
            return f(x + 1, h + 1) and f(x + 4, h + 1) and f(x * 5, h + 1)

for x in range(1, 68):
    if f(x, 0) == 1:
        print(x)