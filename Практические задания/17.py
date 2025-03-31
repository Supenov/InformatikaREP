
al = [int(x) for x in open('17.txt')]

for i in range(len(al) - 1):
    a, b = al[i:i+2]
    print(a, b) ; break