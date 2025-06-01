m = 0
box = []

for x in range(1, 2031):
    n = 7 ** 170 + 7 ** 100 - x

    zero_counter = 0

    while n > 0:
        if n % 7 == 0:
            zero_counter += 1
        n = n // 7
    
    #m = max(zero_counter, m)
    #box.append(m)

    # if zero_counter == 73:
    #     print(x)

    if zero_counter >= m:
        m = zero_counter
        print(x, zero_counter)

#print(max(box))