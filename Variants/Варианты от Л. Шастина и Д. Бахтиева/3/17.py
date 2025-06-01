file = open('17_18176.txt')
lst = [int(x) for x in file]

mn_4 = min(x for x in lst if x > 0 and str(abs(x))[-1] == '4')

def sum_nums(number):
    number = int(str(number).replace('-', ''))

    return sum(int(x) for x in str(number))

box = []
for i in range(len(lst)-2):
    a, b, c = lst[i:i+3]

    if sum_nums(a) + sum_nums(b) + sum_nums(c) == mn_4:
        box.append(a+b+c)

print(len(box), max(box))