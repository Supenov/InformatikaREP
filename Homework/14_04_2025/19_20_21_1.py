# В первой куче было 10 камней ; во второй s2 > 10

def game(s1, s2, m):
    if s1 + s2 <= 20:
        return 1
    if m == 0:
        return 0
    
    actions = [
        game(s1 - 1, s2, m - 1), game(s1, s2 - 1, m),
        game(s1 // 2 + 1, s2, m - 1), game(s1, s2 // 2 + 1, m - 1)
    ]

    return any(actions) if (m - 1) % 2 == 0 else any(actions)


print(19, [s2 for s2 in range(11, 200) if game(10, s2, 2)]) # 11
print(20, [s2 for s2 in range(11, 200) if game(10, s2, 3) and not game(10, s2, 1)])
print(21, [s2 for s2 in range(11, 200) if game(10, s2, 4) and not game(10, s2, 2)])