from itertools import combinations
import random
import time

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

def generate_random_graph(num_vertices, edge_probability):
    graph = {i: [] for i in range(num_vertices)}
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if random.random() < edge_probability:
                graph[i].append(j)
                graph[j].append(i)
    return graph

def measure_time_complexity():
    sizes = list(range(2, 30, 2))  # Adjust the range for larger sizes if needed
    times = []
    edge_probability = 0.5
    for size in sizes:
        graph = generate_random_graph(size, edge_probability)
        start_time = time.time()
        max_clique = find_cliques(graph)
        end_time = time.time()
        times.append(end_time - start_time)
        print(f"Graph size: {size}, Time taken: {end_time - start_time:.4f} seconds, Maximum clique size: {len(max_clique)}")
        
    import matplotlib.pyplot as plt

    plt.plot(sizes, times, marker='o')
    plt.xlabel('Graph size')
    plt.ylabel('Time taken (seconds)')
    plt.title('Time Complexity of Finding Maximum Clique')
    plt.grid(True)
    plt.show()

# Example usage:
random.seed(42)  # For reproducibility
measure_time_complexity()