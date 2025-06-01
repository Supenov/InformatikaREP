from re import *

s = open("24_20968.txt").readline()
s = s.replace('*', 'A')
s = s.replace('+', 'B')

number = r"([1-9][0-9]*[02468] | [02468])"

reg = rf"{number}([AB]{number})+"

s = s[:100]
print(s)

for i in finditer(reg, s):
    print(i)