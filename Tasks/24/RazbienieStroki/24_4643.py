s = open('24_4643.txt').readline()

s = s.replace('B', 'A').replace('2', '1')
s = s.replace('11A', '*').replace('A', ' ').replace('1', ' ')
print( max( len(x) for x in s.split() ) )