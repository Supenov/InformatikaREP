# +1 ; *2
# 1 <= S <= 41
# S1 = 8

def f(s1, s2, h):
    if h == 2 and s1 + s2 >= 50:
        return 1
    elif h == 2 and s1 + s2 < 50:
        return 0
    elif s1 + s2 >= 50 and h < 2:
        return 0
    else:
        if h % 2 == 1:
            return f(s1 +1, s2, h + 1) or f(s1, s2 + 1, h + 1)\
                or f(s1 * 2, s2, h + 1) or f(s1, s2 * 2, h + 1)
        else:
            return f(s1 + 1, s2, h + 1) or f(s1, s2 + 1, h + 1) \
                or f(s1 * 2, s2, h + 1) or f(s1, s2 * 2, h + 1)

for s2 in range(1, 42):
    if f(8, s2, 0) == 1:
        print(s2)
        break