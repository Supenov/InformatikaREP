def sum_numbers(s):
    string = s.replace('>', '')
    return sum(int(x) for x in string)



for n in range(6, 101):
    s = ">" + "0" * 19 + "1" * n + "2" * 19

    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)
    
    
    if str(sum_numbers(s))[-1] ==  str(sum_numbers(s))[-2]:
        print(n)
        break