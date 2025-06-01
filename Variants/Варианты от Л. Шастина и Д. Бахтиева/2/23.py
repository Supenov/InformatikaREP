def f(begin, end):
    if begin < end or begin == 24:
        return 0
    if begin == end:
        return 1

    return f(begin - 2, end) + f(begin - 3, end) + f(begin // 4, end)

print(f(36, 13))