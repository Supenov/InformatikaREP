# +1 ; +2 ; *2

def f(s, m):
    if m == 2 and s >= 37:
        return 1
    elif m == 2 and s < 37:
        return 0
    elif m < 3 and s >= 37:
        return 0
    else:
        if m % 2 == 0:
            return f(s+1, m + 1) or f(s+2, m + 1) or f(s*2, m + 1)
        else:
            return f(s+1, m + 1) or f(s+2, m + 1) or f(s*2, m + 1)

for x in range(1, 38):
    if f(x, 0) == 1:
        print(x)
        break