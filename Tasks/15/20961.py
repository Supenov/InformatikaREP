def f(x, a1, a2):
    P = 15 <= x <= 142
    Q = 38 <= x <= 167
    A = a1 <= x <= a2

    return not(Q <= ( ( (not A) and P ) <= (not Q) ) )

answer =[]
for a1 in range(14, 168):
    for a2 in range(a1+1, 169):
        if all(f(x, a1, a2) == 0 for x in range(0, 300)):
            answer.append(a2-a1)

print(min(answer))