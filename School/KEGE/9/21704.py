k = 0
c = 0
box = []

for s in open("21704.txt"):
    c += 1

    a = sorted([int(x) for x in s.split()], reverse=True)
    #print(a, a[0], a[6])
    if (a[0] + a[6]) // 2 > (a[1] + a[2] + a[3] + a[4] + a[5]) // 5:
        box.append((a, c))

print(min(box))



# print(sum(x for x in min(box[0])))

