s = open('24_21.txt').readline()

while 'XX' in s or 'ZZ' in s or 'YY' in s:
    if 'XX' in s:
        s = s.replace('XX', 'X X')
    if 'ZZ' in s:
        s = s.replace('ZZ', 'Z Z')
    if 'YY' in s:
        s = s.replace('YY', 'Y Y')

print( max(len(c) for c in s.split() ) )