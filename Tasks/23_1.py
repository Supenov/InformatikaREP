def f(begin, end):
    if begin > end or begin == 15:
        return 0
    if begin == end:
        return 1
    return f(begin + 1, end) + f(begin + 2, end)

print( f(3, 9) * f(9, 20) )