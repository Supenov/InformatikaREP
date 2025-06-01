file = open('26var15.txt')
s, n = map(int, file.readline().split())

sizes = [int(s) for s in file]
sizes.sort()