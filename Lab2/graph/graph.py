import matplotlib.pyplot as plt
import networkx as nx
import random
import string
import pandas as pd

class Graph:
    def __init__(self, directed = True):
        self.__graph = {}
        self.__directed = directed
        self.__vertices = 0
        self.__edges = 0
        self.type = "Directed" if directed else "Undirected"
        print(f"New {self.type} Graph created successfully.")

    def add_vertex(self, vertex: str):
        if vertex not in self.__graph:
            print(f"Adding vertex {vertex} to the graph.")
            self.__graph[vertex] = {}
            self.__vertices += 1
        else:
            print(f"Vertex {vertex} already exists in the graph.")

    def __add_undirected_edge(self, vertex1:str, vertex2:str, weight:int):
        if self.__directed:
            print("The given graph is directed. Use add_directed_edge() method instead.")
        else:
            if vertex1 in self.__graph and vertex2 in self.__graph:
                if vertex2 in self.__graph[vertex1] or vertex1 in self.__graph[vertex2]:
                    print(f"Edge of weight {self.__graph[vertex1][vertex2]} already exists between {vertex1} and {vertex2}.")
                else:
                    self.__graph[vertex1].update({vertex2: weight})
                    self.__graph[vertex2].update({vertex1: weight})
                    print(f"Adding undirected edge between {vertex1} and {vertex2} with weight {weight}.")
                    self.__edges += 1
            else:
                print("One or more vertices not found in the graph.")
    
    def __add_directed_edge(self, vertex1:str, vertex2:str, weight:int):
        if not self.__directed:
            print("The given graph is undirected. Use add_undirected_edge() method instead.")
        else:
            if vertex1 in self.__graph and vertex2 in self.__graph:
                if vertex2 in self.__graph[vertex1]:
                    print(f"Edge of weight {self.__graph[vertex1][vertex2]} already exists from {vertex1} to {vertex2}.")
                else:
                    self.__graph[vertex1].update({vertex2: weight})
                    print(f"Adding directed edge from {vertex1} --> {vertex2} with weight {weight}.")
                    self.__edges += 1
            else:
                print("One or more vertices not found in the graph.")
    
    def add_edge(self, vertex1:str, vertex2:str, weight:int = 1):
        if self.__directed:
            self.__add_directed_edge(vertex1, vertex2, weight)
        else:
            self.__add_undirected_edge(vertex1, vertex2, weight)
    
    def remove_vertex(self, vertex:str):
        if vertex in self.__graph:
            print(f"Removing vertex {vertex} from the graph.")
            del self.__graph[vertex]
            self.__vertices -= 1
            for other_vertex in self.__graph:
                if vertex in self.__graph[other_vertex]:
                    del self.__graph[other_vertex][vertex]
                    self.__edges -= 1
        else:
            print(f"Vertex {vertex} not found in the graph.")
    
    def remove_edge(self, vertex1:str, vertex2:str):
        if vertex1 in self.__graph and vertex2 in self.__graph:
            if self.__directed:
                if vertex2 in self.__graph[vertex1]:
                    print(f"Removing directed edge of weight {self.__graph[vertex1][vertex2]} from {vertex1} --> {vertex2}.")
                    del self.__graph[vertex1][vertex2]
                    self.__edges -= 1
                else:
                    print(f"No edge from {vertex1} to {vertex2} found.")
            else:
                if vertex2 in self.__graph[vertex1] or vertex1 in self.__graph[vertex2]:
                    print(f"Removing undirected edge between {vertex1} and {vertex2} with weight {self.__graph[vertex1][vertex2]}.")
                    del self.__graph[vertex1][vertex2]
                    del self.__graph[vertex2][vertex1]
                    self.__edges -= 1
                else:
                    print(f"No edge between {vertex1} and {vertex2} found.")
        else:
            print("One or more vertices not found in the graph.")
            
    def number_of_vertices(self):
        return self.__vertices

    def number_of_edges(self):
        return self.__edges
    
    def update_edge(self, vertex1:str, vertex2:str, weight:int):
        if vertex1 in self.__graph and vertex2 in self.__graph:
            if self.__directed:
                if vertex2 in self.__graph[vertex1]:
                    print(f"Updating weight of directed edge from {vertex1} --> {vertex2} from {self.__graph[vertex1][vertex2]} to {weight}.")
                    self.__graph[vertex1][vertex2] = weight
                else:
                    print(f"No edge from {vertex1} to {vertex2} found.")
            else:
                if vertex2 in self.__graph[vertex1] or vertex1 in self.__graph[vertex2]:
                    print(f"Updating weight of undirected edge between {vertex1} and {vertex2} from {self.__graph[vertex1][vertex2]} to {weight}.")
                    self.__graph[vertex1][vertex2] = weight
                    self.__graph[vertex2][vertex1] = weight
                else:
                    print(f"No edge between {vertex1} and {vertex2} found.")
        else:
            print("One or more vertices not found in the graph.")
            
    def plot_graph(self):
        # Use different layouts for better visualization
        layout = nx.circular_layout(self.__graph) if self.__vertices <= 10 else nx.spring_layout(self.__graph)
        
        G = nx.DiGraph() if self.__directed else nx.Graph()

        # Add edges and weights to the networkx graph
        for vertex1, edges in self.__graph.items():
            for vertex2, weight in edges.items():
                G.add_edge(vertex1, vertex2, weight=weight)

        # Draw the graph
        plt.figure(figsize=(10, 8))  # Adjust the figure size for better clarity
        nx.draw(
            G, 
            pos=layout, 
            with_labels=True, 
            node_size=1000, 
            node_color="skyblue", 
            font_weight="bold", 
            font_size=10,
            edge_color="gray"
        )

        # Draw edge labels (weights)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos=layout, edge_labels=edge_labels, font_size=8, label_pos=0.5)

        # Add a title to the graph
        plt.title(f"{self.type} Graph with {self.__vertices} vertices and {self.__edges} edges", fontsize=14)
        plt.show()
    
    def display_adjacency_matrix(self):
        # Get the list of vertices
        vertices = list(self.__graph.keys())
        num_vertices = len(vertices)

        # Create an empty matrix
        matrix = [[0] * num_vertices for _ in range(num_vertices)]
        
        # Fill the matrix based on the graph's edges
        vertex_indices = {vertex: i for i, vertex in enumerate(vertices)}
        for vertex1, edges in self.__graph.items():
            for vertex2, weight in edges.items():
                i, j = vertex_indices[vertex1], vertex_indices[vertex2]
                matrix[i][j] = weight
                if not self.__directed:
                    matrix[j][i] = weight

        # Create a DataFrame for better readability
        df = pd.DataFrame(matrix, index=vertices, columns=vertices)
        print("Adjacency Matrix:")
        print(df)

    def display(self):
        for vertex in self.__graph:
            print(f"{vertex}: {self.__graph[vertex]}")
    
    def get_vertices(self):
        return list(self.__graph.keys())
    
    def get_edges(self):
        edges = []
        for vertex1, edge in self.__graph.items():
            for vertex2, weight in edge.items():
                if self.__directed:
                    edges.append((vertex1, vertex2, weight))
                else:
                    if (vertex2, vertex1, weight) not in edges:
                        edges.append((vertex2, vertex1, weight))
        return edges
    
    def get_adjacent_vertices(self, vertex:str):
        return list(self.__graph[vertex].keys())
    
    def get_edge_weight(self, vertex1:str, vertex2:str):
        if vertex1 in self.__graph and vertex2 in self.__graph[vertex1]:
            return self.__graph[vertex1][vertex2]
        else:
            print("One or more vertices not found in the graph.")
            return None

    def __str__(self):
        return f"{self.type} Graph with {self.__vertices} vertices and {self.__edges} edges."

def generate_random_graph(graph: Graph, num_vertices: int, num_edges: int, max_weight: int = 10):
    """
    Generates a random graph with specified vertices, edges, and weights.

    Parameters:
    - graph (Graph): The graph object to populate.
    - num_vertices (int): Number of vertices to generate.
    - num_edges (int): Number of edges to generate.
    - max_weight (int): Maximum weight for edges (default: 10).

    Returns:
    None
    """
    if num_vertices > len(string.ascii_uppercase):
        print("Error: Cannot create more vertices than there are capital letters.")
        return
    total_possible_edges = num_vertices * (num_vertices - 1) if graph.type == "Directed" else num_vertices * (num_vertices - 1) / 2
    if (total_possible_edges < num_edges):
        print("Error: Cannot create more edges than the total possible edges.")
        return

    # Generate random vertices
    vertices = random.sample(string.ascii_uppercase, num_vertices)
    print(f"Generated vertices: {vertices}")

    for vertex in vertices:
        graph.add_vertex(vertex)

    # Generate random edges
    possible_edges = [(v1, v2) for v1 in vertices for v2 in vertices if v1 != v2]
    if graph.type == "Undirected":
        for v1, v2 in possible_edges:
            if (v2, v1) in possible_edges:
                possible_edges.remove((v2, v1))
    random_edges = random.sample(possible_edges, min(num_edges, len(possible_edges)))

    for v1, v2 in random_edges:
        weight = random.randint(1, max_weight)
        graph.add_edge(v1, v2, weight)

    print(f"Added {len(random_edges)} random edges.")