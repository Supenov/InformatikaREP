def convert_base(num):
    string = ''
    while num > 0:
        string = str(num%5) + string
        num //= 5
    return string


for x in range(1, 5555):
    number = 5 ** 150 + 5 ** 135 - x
    converted_number = convert_base(number)

    if converted_number.count('4') == 134:
        print(x)