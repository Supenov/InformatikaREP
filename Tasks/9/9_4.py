k = 0

file = open("9_4.txt")

for i in file:
    a = sorted([int(x) for x in i.split()])

    pov2 = set(x for x in a if a.count(x) == 2)
    nepov = [x for x in a if a.count(x) == 1]

    if pov2 and len(nepov) == 2:
        k += 1



print(k)


# k = 0
#
# with open("9_4.txt") as file:
#     for line in file:
#         nums = list(map(int, line.strip().split()))
#
#         counts = {}
#         for num in nums:
#             counts[num] = counts.get(num, 0) + 1
#
#         pov2 = tuple(num for num, cnt in counts.items() if cnt == 2)
#         nepov = [num for num, cnt in counts.items() if cnt == 1]
#
#         # Условие 1: только одно число повторяется дважды
#         if len(pov2) != 1:
#             continue
#
#         # Условие 2: повторяющееся число четное
#         if pov2[0] % 2 != 0:
#             continue
#
#         # Условие 3: неповторяющиеся числа нечетны и их должно быть ровно 2
#         if len(nepov) != 2:
#             continue
#
#         if all(x % 2 != 0 for x in nepov):
#             k += 1
#
# print(k)