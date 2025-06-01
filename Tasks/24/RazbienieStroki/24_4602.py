s = open('24_4602.txt').readline()

s = s.replace('O', 'A').replace('C', 'B').replace('D', 'B')

s = s.replace('BA', '*').replace('A', ' ').replace('B', ' ')

print(max( len(c) for c in s.split() ) )
