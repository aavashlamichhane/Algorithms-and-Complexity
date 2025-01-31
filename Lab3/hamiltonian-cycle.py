import random
import time
import matplotlib.pyplot as plt
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

def generate_random_graph(n, edge_probability=0.5):
    graph = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < edge_probability:
                graph[i][j] = graph[j][i] = 1
    return graph

def measure_time(n):
    graph = generate_random_graph(n)
    start_time = time.time()
    hamiltonian_cycle(graph)
    end_time = time.time()
    return end_time - start_time

sizes = range(2, 15, 1)  # Adjust the range for larger sizes if needed
times = []

for size in sizes:
    elapsed_time = measure_time(size)
    times.append(elapsed_time)
    print(f"Size: {size}, Time: {elapsed_time:.6f} seconds")

plt.plot(sizes, times, marker='o')
plt.xlabel('Graph Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Time Complexity of Hamiltonian Cycle Algorithm')
plt.grid(True)
plt.show()