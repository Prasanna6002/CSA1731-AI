import heapq
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 5)],
    'C': [('F', 2)],
    'D': [('G', 3)],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}
h = {
    'A': 5, 'B': 4, 'C': 3,
    'D': 2, 'E': 2, 'F': 1, 'G': 0
}
def astar(start, goal):
    queue = [(h[start], 0, start, [start])]
    best_cost = {start: 0}
    while queue:
        _, cost, node, path = heapq.heappop(queue)
        if node == goal:
            print("Path:", path)
            print("Cost:", cost)
            return
        if cost > best_cost.get(node, float('inf')):
            continue
        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < best_cost.get(neighbor, float('inf')):
                best_cost[neighbor] = new_cost
                priority = new_cost + h[neighbor]
                heapq.heappush(
                    queue,
                    (priority, new_cost, neighbor,
                     path + [neighbor])
                )
    print("Path not found")
astar('A', 'G')