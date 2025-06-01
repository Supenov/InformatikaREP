s = open('24_1040.txt').readline()

for x in "qwertyuiopasdfghjklzxcvbnm":
    s = s.replace(x, ' ')

print( max( len(c) for c in s.split() ) )
