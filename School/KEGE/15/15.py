p = set(range(17, 59))
q = set(range(29, 81))
a = set()

def f(x):
    P = x in p
    Q = q in q
    A = x in a

    #return not(x in P) <= ( ((x in Q) and (x in A)) <= (not (x in P)))
    return P <=  ( (Q and (not A)) <= (not (P)))

for x in range(1, 1000):
    if not(f(x)):
        a.add(x)



print(len(a))

