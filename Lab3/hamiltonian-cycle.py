from itertools import permutations

def is_valid_cycle(graph, cycle):
    n = len(graph)
    for i in range(n):
        if not graph[cycle[i]][cycle[(i + 1) % n]]:
            return False
    return True

def hamiltonian_cycle(graph):
    n = len(graph)
    vertices = list(range(n))
    for perm in permutations(vertices[1:]):
        cycle = [0] + list(perm)
        if is_valid_cycle(graph, cycle):
            return cycle
    return None

# Example usage:
graph = [
    [0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 0, 1],
    [1, 1, 0, 1, 0]
]

cycle = hamiltonian_cycle(graph)
if cycle:
    print("Hamiltonian Cycle found:", cycle)
else:
    print("No Hamiltonian Cycle found")