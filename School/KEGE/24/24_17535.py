s = open('24_17535.txt').readline()

l = 0
m = 0
k = 0

for r in range(1, len(s)):
    if s[r - 1] + s[r] == 'CD':
        k += 1
        
    while k > 160:
        if s[l] + s[l + 1] == 'CD':
            k -= 1
        l += 1
    
    if k == 160:
        m = max(m, r - l + 1)

print(m)