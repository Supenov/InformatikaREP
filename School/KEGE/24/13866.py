s = open('24_13866.txt').readline()

k = 2
m = 0

for r in range(len(s) - 2):
    if not(s[r] in '13579' and s[r+1] in '13579' and s[r+2] in '13579'):
        k += 1
        m = max(m , k)
    else:
        k = 2
print(m)