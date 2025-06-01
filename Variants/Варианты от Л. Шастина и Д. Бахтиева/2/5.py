box = []

for n in range(1, 100):
    b = bin(n)[2:]

    if n % 5 == 0:
        b = b[:3] + b
    else:
        ost = n % 5
        b += bin(ost*5)[2:]

    R = int(b, 2)

    if R < 313:
        if n % 2 != 0 :
            box.append(n)

print(max(box))