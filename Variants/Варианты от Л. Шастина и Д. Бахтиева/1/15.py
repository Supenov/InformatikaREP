P = set(range(12, 63))
Q = set(range(52, 93))
A = set(range(10, 1001))

def f(x):

    return not( (x not in A)  and (x in P) ) or (x in Q)

for x in range(1, 1000):
    if f(x) == 0:
        print(x)
