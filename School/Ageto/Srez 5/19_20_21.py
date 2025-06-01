def game(s, m):
    if s <= 19:
        return m % 2 == 0
    if m == 0:
        return 0
    
    actions = [
        game(s - 2, m - 1),
        game(s - 5, m - 1),
        game(s // 3, m - 1)
    ]
    return any(actions) if m % 2 != 0 else all(actions)


print("19", [s for s in range(300, 21, -1) if game(s, 2)]) # 61 60
print("20", [s for s in range(300, 21, -1) if game(s, 3) and not(game(s, 1))]) # [185, 184, 183, 182, 181, 180, 66, 65, 63, 62]
print("21", [s for s in range(300, 21, -1) if game(s, 4) and not(game(s, 2))])

