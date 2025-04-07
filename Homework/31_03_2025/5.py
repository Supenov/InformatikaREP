box = []

for n in range(100, 1000):
    stSum = int(str(n)[0]) + int(str(n)[1])
    sdSum = int(str(n)[1]) + int(str(n)[2])

    totalSum = int( str(max(stSum, sdSum)) + str(min(stSum, sdSum)) ) 

    if totalSum == 1412:
        box.append(n)

print(min(box))

# 395