def perevod(n):
    string = ""
    while n > 0:
        string = str(n % 8) + string
        n = n // 8
    return string


def replacer_even(s):
    for x in "13579":
        s = s.replace(x, "2")
    return s


def replacer_odd(s):
    s = s.replace(s[0], "3").replace(s[-1], "3")

    return s


box = []
for n in range(1, 10_000):
    e = perevod(n)


    if n % 2 == 0:
        new_e = replacer_even(e)
    else:
        new_e = replacer_odd(e)
    
    R = int(new_e, 8)
    
    if R < 300:
        box.append(R)



print(max(box))