# +3; +8; *2

def f(s, h):
    if s >= 333:
        return h % 2 == 0
    if h == 0:
        return 0

    a = [
        f(s + 3, h - 1),
        f(s + 8, h - 1),
        f(s * 2, h - 1)
    ]

    return any(a) if (h - 1) % 2 == 0 else all(a)

print([s for s in range(1, 333) if f(s, 2)])
print([s for s in range(1, 333) if f(s, 3) and not f(s, 1)])
print([s for s in range(1, 333) if f(s, 4) and not f(s, 2)])