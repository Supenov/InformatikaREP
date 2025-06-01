# +1 ; +4 ; *5

def f(x, h):
    if h == 2 and x >= 68: # Если ход Вани и у него нужное количество камней, возвращаем истину
        return 1
    elif h == 2 and x < 68: # Если ход Вани и у Вани недостаточно камней возвращаем ложь
        return 0
    elif h < 3 and  x >= 68: # Если ход Пети, а Ваня не выиграл возвращаем ложь
        return 0
    else:
        if h % 2 == 0:
            return f(x + 1, h + 1) or f(x + 4, h + 1) or f(x * 5, h + 1)
        else:
             return f(x + 1, h + 1) or f(x + 4, h + 1) or f(x * 5, h + 1) # Заменяем or на and если при любом ходе Пети Ваня выигрывает

for x in range(1, 68): # 1 <= S <= 68
    if f(x, 0) == 1:
        print(x)
        break


# def game(s, m):
#     if s >= 68:
#         return m % 2 == 0
#     if m == 0:
#         return 0
#
#     actions = [
#         game(s + 1, m - 1), game(s + 4, m - 1), game(s * 5, m - 1)
#     ]
#
#     return any(actions) if (m - 1) % 2 == 0 else any(actions)
#
# print(19, [s for s in range(1, 68) if game(s, 2)])