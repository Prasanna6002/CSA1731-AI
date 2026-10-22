from collections import deque
def water_jug(a, b, target):
    q = deque([(0, 0)])
    visited = set()
    while q:
        x, y = q.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        print(x, y)
        if x == target or y == target:
            print("Target reached")
            return
        q.append((a, y))
        q.append((x, b))
        q.append((0, y))
        q.append((x, 0))
        p = min(x, b - y)
        q.append((x - p, y + p))
        p = min(y, a - x)
        q.append((x + p, y - p))
water_jug(4, 3, 2)