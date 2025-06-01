def f(begin, end):
    if begin < end or begin == 26 or begin == 30:
        return 0
    if begin == end:
        return 1

    return f(begin - 3, end) + f(begin // 2, end)

print(f(69, 14))