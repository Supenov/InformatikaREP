s = open('24_12476.txt').readline()

while 'ORO' in s or 'ROR' in s:
    if 'ORO' in s:
        s = s.replace('ORO', ' ') #s = s.replace('ORO', 'OR RO')
    if 'ROR' in s:
        s = s.replace('ROR', ' ') #s = s.replace('ROR', 'RO OR')
s = s.split()

box = []
for i in s:
    if i.count('RO') == 21:
        print(len(i))
        box.append(len(i))
print(max(box))



#print( max( len(c) for c in s if s.count('RO') == 21 ) )

# l = 0
# m = 0
# kRO = 1

# for r in range(1, len(s)):
#     if s[r - 1] + s[r] == 'RO':
#         kRO += 1
#     while kRO > 21:
#         if s[l] + s[l + 1] == 'RO':
#             kRO -= 1
#         l += 1
#     if kRO == 21:
#         m = max(m, r - l + 1)

# print(m)