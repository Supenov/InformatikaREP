# +1; *3

def f(s, h):
    if s >= 65:
        return h % 2 == 0
    if h == 0:
        return 0
    a = [f(s+1, h -1),
         f(s*3, h -1)]

    return any(a) if (h - 1) % 2 == 0 else all(a) # Меняется all на any если неудачный ход Пети



print([s for s in range(1, 65) if f(s, 2)]) # 8
print([s for s in range(1, 65) if f(s, 3) and not f(s, 1)] ) # 7 20
print([s for s in range(1, 65) if f(s, 4) and not f(s, 2)] ) # 19