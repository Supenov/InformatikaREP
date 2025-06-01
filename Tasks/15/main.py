# Номер 1
def f(x, a1, a2):
    B = 36 <= x <= 75
    C = 60 <= x <= 110
    A = a1 <= x <= a2

    return (not A) <= (B == C)

ans = []
for a1 in range(35, 111):
    for a2 in range(a1 + 1, 112):
        if all(f(x,a1, a2) == 1 for x in range(30, 115)):
            ans.append(a2-a1)
print(min(ans))


# # Номер 2
# def f2(x, a1, a2):
#     P = 15 <= x <= 142
#     Q = 38 <= x <= 167
#     A = a1 <= x <= a2
#
#     return (not(Q <= (((not A) and P) <= (not Q))))
#
# new_ans = []
# for a1 in range(14, 168):
#     for a2 in range(a1 + 1, 169):
#         if all(f2(x,a1, a2) == 0 for x in range(10, 175)):
#             new_ans.append(a2-a1)
# print(min(new_ans))


# # Номер 3
# def f3(x, a1, a2):
#     P = 17 <= x <= 58
#     Q = 29 <= x <= 80
#     A = a1 <= x <= a2
#
#     return P <= ( (Q and (not(A))) <= (not (P)) )
#
# ans3 = []
# for a1 in range(16, 81):
#     for a2 in range(a1 + 1, 82):
#         if all(f3(x, a1, a2) == 1 for x in range(12, 95)):
#             ans3.append(a2 - a1)
# print(min(ans3))


# # Номер 4
# def f4(x, a1, a2):
#     P = 17 <= x <= 54
#     Q = 37 <= x <= 83
#     A = a1 <= x <= a2
#
#     return P <= ( (Q and (not(A))) <= (not (P)) )
#
# ans4 = []
# for a1 in range(13, 84):
#     for a2 in range(a1 + 1, 85):
#         if all(f4(x, a1, a2) == 1 for x in range(10, 90)):
#             ans4.append(a2 - a1)
#
# print(min(ans4))
