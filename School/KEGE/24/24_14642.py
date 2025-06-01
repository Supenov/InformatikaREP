s = open('24.3_14642.txt').readline()

l = 0
m = 0
k = 0


for r in range(len(s)):
    if s[r] == 'F':
        k += 1
    while k > 1:
        if s[l] == 'F':
            k -= 1
        l += 1
    m = max(m, r - l + 1)

print(m)