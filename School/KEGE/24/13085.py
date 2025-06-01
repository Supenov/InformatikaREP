s = open('24_13085.txt').readline()

l = 0
m = 0
kx = ky = 1


for r in range(len(s)):
    if s[r] == 'X':
        kx += 1
    if s[r] == 'Y':
        ky += 1
    
    while kx > 1 or ky > 1:
        if s[l] == 'X':
            kx -= 1
        if s[l] == 'Y':
            ky -= 1
    m = max(m, r - l + 1)

print(m)