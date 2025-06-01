# +1 ; +3 ; *2

def f(x, h):
    if h == 3 and x >= 54:
        return 1
    elif h == 3 and x < 54:
        return 0
    elif x >= 54 and h < 3:
        return 0
    else:
        if h % 2 == 1:
            return f(x + 1, h + 1) and \
                f(x + 3, h + 1) and \
                f(x * 2, h + 1)
        else:
            return f(x + 1, h + 1) or \
                f(x + 3, h + 1) or \
                f(x * 2, h + 1)

for x in range(1, 54):
    if f(x, 0) == 1:
        print(x)
