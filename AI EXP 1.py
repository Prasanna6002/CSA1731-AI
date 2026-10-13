from collections import deque

g = {
    0:[1,2],
    1:[0,3,4],
    2:[0,4],
    3:[1],
    4:[1,2]
}
def bfs(start):
    q = deque([start])
    visited = {start}
    print ("BFS Traversal:", end =" ")
    while q:
        v = q.popleft()
        print(v, end = " ")

        for n in g[v]:
            if n not in visited:
                visited.add(n)
                q.append(n)
    print()
if __name__ == "__main__":
    print("program started")
    bfs(0)
            
