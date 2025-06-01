from re import *

s = open('24_19884.txt').readline()

num = r"[1-9][0-9]*"

pat = rf"{num}(?:[-*]{num})+"

print(findall(pat, s))

print( max( map(len, findall(pat, s)) ))

# Неверно решено