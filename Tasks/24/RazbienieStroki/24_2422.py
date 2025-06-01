s = open('24_2422.txt').readline()
print(s[:100])
while 'XY' in s or 'YZ' in s or 'XYZ' in s or 'XZ' in s:
    if 'XYZ' in s:
        s = s.replace('XYZ', '*')
    if 'XY' in s:
        s = s.replace('XY', '*')
    if 'YZ' in s:
        s = s.replace('YZ', '*')
    if 'XZ' in s:
        s = s.replace('XZ', '*')


s = s.replace('X', ' ').replace('Y', ' ').replace('Z', ' ')
print(s[:100])
print(max(len(c) for c in s.split() ) )