for i in range(700_001, 10**40):
    d = []
    for j in range(2, i):
        if i % j == 0:
            d.append(j)
    if d:
        M = d[0] + d[-1]
    else:
        M = 0
    if str(M)[-1] == '8':
        print(i, M)

'''
700005 233338
700007 100008
700012 350008
700015 140008
700031 24168
'''