file = open('9.txt')

k = 0
for i in file:


    a = sorted([int(x) for x in i.split()])
    b = a.copy()

    sum_nechet = 0
    sum_chet = 0
    mx = b.pop()

    for x in a:
        if x % 2 != 0:
            sum_nechet += x
        else:
            sum_chet += x

    if (mx < sum(b)) and sum_chet == sum_nechet:
        k += 1
        # print(k, a, sum_chet, sum_nechet)

print(k)

# 13