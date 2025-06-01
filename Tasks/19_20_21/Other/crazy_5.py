# -5; //3;

def f(s, h):
    if s <= 19:
        return h % 2 == 0
    if h == 0:
        return 0

    a = [f(s-5, h-1)]

    if s % 2 == 0:
        a.append(f(s // 2, h - 1))
    if s % 3 == 0:
        a.append(f(s // 3, h - 1))
    if s % 2 != 0 and s % 3 != 0:
        a.append(f(s + 1, h - 1))
    return any(a) if (h - 1) % 2 == 0 else all(a)

print([s for s in range(20, 100) if f(s, 2)])                       # 25
print([s for s in range(20, 100) if f(s, 3) and not f(s, 1)]) # 40, 43
print([s for s in range(20, 100) if f(s, 4) and not f(s, 2)]) # 60
