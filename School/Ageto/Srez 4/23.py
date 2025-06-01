def f(begin, end):
    if begin < end:
        return 0
    if begin == end:
        return 1
    
    return f(begin - 2, end) + f(begin // 2, end)

print(f(38, 16)* f(16, 2))
