m = 0
box = []

for x in range(1, 2006):
    
    zero_counter = 0
    n = 5 ** 150 + 5 ** 98 - x

    while n > 0:
        if n % 5 == 0:
            zero_counter += 1
        n = n // 5

    #m = max(zero_counter, m)
    #box.append(m)

    if zero_counter == 56:
        print(x)

#print(max(box))