def game(s, move):
    if s >= 58:
        return move % 2 == 0
    if move == 0:
        return 0
    
    actions = [
        game(s + 1, move - 1),
        game(s + 4, move - 1),
        game(s * 2, move - 1)
    ]

    return any(actions) if move % 2 != 0 else all(actions)


print("19", [s for s in range(1, 58) if game(s, 2)]) # [28]
print("20", [s for s in range(1, 58) if game(s, 3) and not(game(s, 1))]) # [14, 24, 27]
print("20", [s for s in range(1, 58) if game(s, 4) and not(game(s, 2))]) # [23, 26]

# 28, 14, 24, 23