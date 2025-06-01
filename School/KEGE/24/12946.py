s = open('24_12946.txt').readline()

for x in 'QWERTYUIOPSDFGHJKLZXCVBNM':
    s = s.replace(x, 'A')
for y in '023456789':
    s = s.replace(y, '1')

while 'AA' in s or '11' in s:
    if 'AA' in s:
        s = s.replace('AA', 'A A')
    if '11' in s:
        s = s.replace('11', '1 1')
s = s.split()

print( max( len(c) for c in s ) )