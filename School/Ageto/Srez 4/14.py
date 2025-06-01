x_box = []

def perevod(number, base):
    box = []
    while number > 0:
        box.append(number % base)
        number = number // base
    
    return box[::-1]


for x in range(1, 2031):
    s = 3**100 - x

    new_s = str(perevod(s, 3))
    if new_s.count("0") == 5:
        x_box.append(x)


print(max(x_box))
