s = open('24_4627.txt').readline()

s = s.replace('NPO', '*').replace('PNO', '*')
s = s.replace('N', ' ').replace('O', ' ').replace('P', ' ')
print( max( len(c) for c in s.split() ) )