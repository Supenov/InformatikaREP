lst = [int(x) for x in open('17_19900.txt')]

sum_4 = sum([x for x in lst if len(str(abs(x))) == 4])

box = []
for i in range(len(lst)-2):
    a, b, c = lst[i:i+3]
    if (  (len(str(abs(a))) == 3) + (len(str(abs(b))) == 3) + (len(str(abs(c))) == 3) ) == 2:
        if (a * b * c) > sum_4:
            box.append(a*b*c)

print(len(box), abs(min(box)))