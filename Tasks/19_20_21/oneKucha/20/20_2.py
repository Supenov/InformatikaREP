# +1 ; +4 ; *5

def f(x, h):
    if h == 3 and x >= 69:
        return 1
    elif h == 3 and x < 69:
        return 0
    elif x >= 69 and h < 3:
        return 0
    else:
        if h % 2 == 0:
            return  f(x + 1, h + 1) or \
                    f(x + 4, h + 1) or \
                    f(x * 5, h + 1)
        else:
            return f(x + 1, h + 1) and \
                f(x + 4, h + 1) and \
                f(x * 5, h + 1)

for x in range(1, 69):
    if f(x, 0) == 1:
        print(x)

print(1 % 2)