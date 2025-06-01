s = open('24_13100.txt').readline()

l = 0
m = 0
kc = kd = 0

for r in range(len(s)):
    if s[r] == 'C':
        kc += 1
    if s[r] == 'D':
        kd += 1

    while kc > 2 or kd > 2:
        if s[l] == 'C':
            kc -= 1
        if s[l] == 'D':
            kd -= 1
        l += 1
        
    m = max(m, r - l + 1)

print(m)