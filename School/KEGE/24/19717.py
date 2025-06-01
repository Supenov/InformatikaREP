s = open('24.5_19717.txt').readline()

l = 0
k = 0
m = 0

for r in range(len(s)):
    if s[r] == 'M':
        k += 1
    while k > 278:
        if s[l] == 'M':
            k -= 1
        l += 1
    m = max(m, r - l + 1)

print(m)

