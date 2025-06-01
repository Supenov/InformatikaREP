# +1; *2
# s1 = 10

def f(s1, s2, h):
    if s1 + s2 <= 20:
        return h % 2 == 0
    if h == 0:
        return 0

    a = [
        f(s1 - 1, s2, h - 1), f(s1, s2 - 1, h - 1),
        f(s1 // 2, s2, h - 1), f(s1, s2 // 2, h - 1)
    ]

    return any(a) if (h - 1) % 2 == 0 else any(a)

print([s2 for s2 in range(10, 100) if f(10, s2, 2)])
# print([s2 for s2 in range(10, 100) if f(10, s2, 3) and not f(10, s2, 1)])
# print([s2 for s2 in range(10, 100) if f(10, s2, 4) and not f(10, s2, 2)])

