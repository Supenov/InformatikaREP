file = open("9_2.txt")

k = 0
for i in file:
    a = sorted([int(x) for x in i.split()])
    b = a.copy()

    mx = a[-1]
    mn = a[0]
    middle = a[1:-1]

    pov = [x for x in a if a.count(x) >= 2]
    nepov = [x for x in a if a.count(x) == 1]

    cond1 = (mn * mx) < (3 * sum(middle))
    cond2 = sum(nepov) <= sum(pov)


    if ((mx * mn) < (3 * sum(middle))) ^ (sum(nepov) <= sum(pov)):
        k += 1

    # if cond1 ^ cond2:
    #     k += 1

print(k)


# with open("9_2.txt") as file:
#     k = 0
#     for line in file:
#         a = sorted([int(x) for x in line.split()])
#         mn = a[0]
#         mx = a[-1]
#         middle = a[1:-1]
#
#         pov = [x for x in a if a.count(x) >= 2]
#         nepov = [x for x in a if a.count(x) == 1]
#
#         cond1 = (mn * mx) < (3 * sum(middle))
#         cond2 = sum(nepov) <= sum(pov)
#
#         if cond1 ^ cond2:  # исключающее ИЛИ
#             k += 1
#
# print(k)