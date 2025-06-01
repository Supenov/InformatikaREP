def f(n):
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return n // d + d
    return 0

c = 0

num = 800_001

while c < 5:
    k = f(num)
    if k % 10 == 4:
        print(num, k)
        c += 1
    num += 1


"""
800004 400004
800009 114294
800013 266674
800024 400014
800033 61554
"""