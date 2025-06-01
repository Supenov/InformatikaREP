s = open('24_18186.txt').readline()

for x in 'CDFGH':
    s = s.replace(x, 'B')
s = s.replace('E', 'A')


s = s.replace('BBA', '*').replace('A', ' ').replace('B', ' ')

print( max( len(c) for c in s.split() ) )

# НЕВЕРНЫЙ ОТВЕТ