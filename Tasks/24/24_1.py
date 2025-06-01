s = open('24.txt.').readline()

s = s.replace('Z',' ').replace('Y', ' ')
#print(s[:100], s.split()[:100])

print(max(len(c) for c in s.split()))

# 19