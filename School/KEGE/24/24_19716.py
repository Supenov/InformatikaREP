s = open('24.21_19716.txt').readline()

k = 1
m = 0

for r in range(len(s) - 1):
    if s[r] != s[r + 1]:
        k += 1
        m = max(m, k)
    else:
        k = 1
print(m)