def f(n):
    if n > 2000:
        return 16
    
    return 2 * f(n + 3)

print(f(50) / f(110))