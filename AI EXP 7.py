from collections import deque
def valid(m, c):
    return (0 <= m <= 3 and 0 <= c <= 3 and
            (m == 0 or m >= c) and
            (m == 3 or 3 - m >= 3 - c))
start = (3, 3, 1)
goal = (0, 0, 0)
q = deque([(start, [])])
visited = {start}
moves = [(1, 0), (2, 0), (0, 1),
         (0, 2), (1, 1)]
while q:
    state, path = q.popleft()
    if state == goal:
        for s in path + [state]:
            print(s)
        break
    m, c, boat = state
    for x, y in moves:
        if boat == 1:
            new = (m - x, c - y, 0)
        else:
            new = (m + x, c + y, 1)
        if valid(new[0], new[1]) and new not in visited:
            visited.add(new)
            q.append((new, path + [state]))