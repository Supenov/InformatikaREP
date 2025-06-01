# +1 ; *2
# 1 <= S <= 69
# S1 = 7 ; S2 = s камней

def f(s1, s2, h):
    if h == 2 and s1 + s2 >= 77:
        return 1
    elif h == 2 and s1 + s2 < 77:
        return 0
    elif h < 3 and s1 + s2 > 77:
        return 0
    else:
        if h % 2 == 0:
            return f(s1 + 1, s2, h + 1) or f(s1, s2 + 1, h + 1)\
                or f(s1 * 2, s2, h + 1) or f(s1, s2 * 2, h + 1)
        else:
            return f(s1 + 1, s2, h + 1) or f(s1, s2 + 1, h + 1)\
                or f(s1 * 2, s2, h + 1) or f(s1, s2 * 2, h + 1)


for x in range(1, 70):
    if f(7, x, 0) == 1:
        print(x)
        break
# 18