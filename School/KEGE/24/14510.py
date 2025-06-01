s = open('24_14510.txt').readline()

def is_letter(n):
    return n.isalpha()

l = 0
m = 0
k = 0

for r in range(2, len(s)):
    if s[r - 2] in 'QWRTPSDFGHJKLZXCVBNM'\
        and s[r - 1] in 'QWRTPSDFGHJKLZXCVBNM'\
        and s[r] in 'AEIOUY':

        k += 1

    if k > 500:
        m = max(m, r - l + 1)

print(m)