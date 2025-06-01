s = open('24_1302.txt').readline()

s = s.replace('XZZY', 'XZZ ZZY')

print( max( len(c) for c in s.split() ) )