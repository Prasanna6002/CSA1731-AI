from itertools import permutations
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
n = len(graph)
cities = range(1, n)
min_cost = float('inf')
best_path = []
for path in permutations(cities):
    tour = (0,) + path + (0,)
    cost = sum(graph[tour[i]][tour[i + 1]]
               for i in range(n))
    if cost < min_cost:
        min_cost = cost
        best_path = tour
print("Best path:", best_path)
print("Minimum cost:", min_cost)