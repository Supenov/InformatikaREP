s = open('24.13_14643.txt').readline()

s = s.replace('AXMM', 'AXM XMM')
s = s.split()

print( max( len(c) for c in s ) )