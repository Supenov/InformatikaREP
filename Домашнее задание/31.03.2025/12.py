box = []

for n in range(101, 1000):
    s = n * '1'

    while '111' in s:
        s = s.replace('111', '22', 1)
        s = s.replace('222', '11', 1)

    box.append(s.count('1'))    
    min_1 = min(box)


for n in range(101, 1000):
    s = n * '1'

    while '111' in s:
        s = s.replace('111', '22', 1)
        s = s.replace('222', '11', 1)
    
    if s.count('1') == min_1:
        print(n) ; break