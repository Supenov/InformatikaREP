
al = [int(x) for x in open('C:/Users/User/Desktop/InformatikaREP/Практические задания/17.txt')]

box = []
for i in range(len(al) - 1):
    a, b = al[i:i+2]
    
    if (a % 3 == 0) or (b % 3 == 0):
        box.append(a+b)

print(len(box), max(box))