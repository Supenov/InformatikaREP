file = open('17.txt')

lst = [int(x) for x in file]

sorted_list = sorted(lst)
mx_mult = sorted_list[-1] * sorted_list[-2]

box = []
for i in range(len(lst) - 2):
    a, b, c = lst[i:i + 3]

    if ( (a < 0) + (b < 0) + (c < 0) == 2 ) and ( (a * b * c) <= mx_mult ):
        box.append(a+b+c)

print(len(box), max(box))