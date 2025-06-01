s = open("24_2420.txt").readline()

s = s.replace("C", "").replace("D", " ")

print( max( len(x) for x in s.split() ) )