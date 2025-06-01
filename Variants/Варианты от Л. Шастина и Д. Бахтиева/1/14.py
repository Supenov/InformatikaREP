n = 7 * 512 ** 120 - 6 * 64 ** 100 + 8 ** 210 - 255

# alphabet = sorted('23456789QWERTYUIOPASDFGHJKLZXCVBNM')

def perevod(n, base):
    string = ''
    while n > 0:
        string = str(n % int(base)) + string
        n = n // int(base)
    return string

for base in range(2, 37):
    if perevod(n, base)[-3:] == '001':
        print(base)

