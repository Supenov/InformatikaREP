def f(begin, end):
    if begin < end or begin == 13:
        return 0
    if begin == end:
        return 1

    return f(begin - 1, end) + f(begin // 2, end) + f(begin // 3, end)

print(f(26, 8) * f(8, 3))