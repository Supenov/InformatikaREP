s = open('24_4113.txt').readline()

s = s.replace('A', ' ')#.replace('BB', '*').replace('DD', '*')

#while 'BB' in s:
s = s.replace('BB', '*')
#while 'DD' in s:
s = s.replace('DD', '*')

s = s.replace('B', ' ').replace('D', ' ')

s = s.split()

print( max( len(c) for c in s ) ) # 316
# Ответ 317