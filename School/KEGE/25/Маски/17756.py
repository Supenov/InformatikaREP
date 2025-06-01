from re import *

s = open('24_17756.txt').readline()

reg = r'[1-9][0-9]*'

pattern = rf'{reg}[+*]{reg}'

#print(max(map(len, findall(pattern, s))))
print(findall(pattern, s))