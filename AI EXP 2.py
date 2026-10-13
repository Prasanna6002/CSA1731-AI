
from collections import deque

goal = "123456780"
start = input("Enter initial state: ")

q = deque([(start, [start])])
visited = {start}

while q:
    state, path = q.popleft()

    if state == goal:
        print("Solution:")
        for s in path:
            print(s[:3])
            print(s[3:6])
            print(s[6:])
            print()
        break

    z = state.index('0')
    r, c = divmod(z, 3)

    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        nr, nc = r + dr, c + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            nz = nr * 3 + nc
            a = list(state)
            a[z], a[nz] = a[nz], a[z]
            new = ''.join(a)

            if new not in visited:
                visited.add(new)
                q.append((new, path + [new]))
else:
    print("No solution found.")
