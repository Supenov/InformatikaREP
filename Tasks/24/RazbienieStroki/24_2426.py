s = open("24_2426.txt").readline()

s = s.replace('A', ' ').replace('B', ' ').replace('C', ' ')

print( max( len(x) for x in s.split() ) )