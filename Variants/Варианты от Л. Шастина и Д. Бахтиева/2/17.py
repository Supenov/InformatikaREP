lst = [int(x) for x in open('17_18045.txt')]

k = 0
for x in lst:
    if len(str(x)) == 2:
        k += 1

box = []
for i in range(len(lst) - 1):
    a, b = lst[i:i+2]
    if ( int(str(a)[-1]) + int(str(b)[-1]) ) == k:
        box.append(a+b)

print(len(box), min(box))