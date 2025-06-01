file = open("9.txt")

k = 0
for i in file:
    a = sorted([int(x) for x in i.split()])
    
    first_treb = [x for x in a if len(str(x)) == 3]
    second_treb = [x for x in a if x % 5 == 0]

    if (len(first_treb) >= 3) and (not second_treb):
        k += 1

print(k)