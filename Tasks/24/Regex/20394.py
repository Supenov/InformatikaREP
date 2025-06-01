s = open("24_20394.txt").readline()

l = 0
m = 0
k = 0

for r in range(len(s)-2):
    if s[r] + s[r+1] + s[r+2] == 'DEC':
        k += 1

    while k > 75:
        if s[l] + s[l+1] + s[l+2] == 'DEC':
            k -= 1
        l += 1

    if k == 75:
        m = max(m, r - l + 3)

print(m)