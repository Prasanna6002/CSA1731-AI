
b = [' '] * 9
wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),
        (1,4,7),(2,5,8),(0,4,8),(2,4,6)]
for t in range(9):
    print(b[0:3], b[3:6], b[6:9])
    p = 'X' if t % 2 == 0 else 'O'
    n = int(input(f"Player {p}, position (1-9): ")) - 1
    if n not in range(9) or b[n] != ' ':
        print("Invalid move!")
        continue
    b[n] = p
    if any(b[a] == b[c] == b[d] == p for a,c,d in wins):
        print(b[0:3], b[3:6], b[6:9])
        print(p, "wins!")
        break
else: print("Draw!")
