
colors = ['Red', 'Green', 'Blue']
graph = {'A': ['B', 'C'], 'B': ['A', 'C', 'D'],
         'C': ['A', 'B', 'D'], 'D': ['B', 'C']}
coloring = {}

def solve(regions):
    if len(coloring) == len(regions):
        return True
    r = regions[len(coloring)]
    for c in colors:
        if all(coloring.get(n) != c for n in graph[r]):
            coloring[r] = c
            if solve(regions): return True
            del coloring[r]
    return False

regions = list(graph)
print(coloring if solve(regions) else "No solution")
