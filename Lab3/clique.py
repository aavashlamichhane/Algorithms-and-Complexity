from itertools import combinations

def is_clique(graph, vertices):
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            if vertices[j] not in graph[vertices[i]]:
                return False
    return True

def find_cliques(graph):
    n = len(graph)
    max_clique = []
    for r in range(1, n + 1):
        for subset in combinations(graph.keys(), r):
            if is_clique(graph, subset):
                if len(subset) > len(max_clique):
                    max_clique = subset
    return max_clique

# Example usage:
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}

print("Maximum clique:", find_cliques(graph))