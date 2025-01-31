from graph.graph import Graph

class Vertex:
    def __init__(self, vertex: str, key: float = float('inf'), root: str = None):
        self.vertex = vertex
        self.key = key
        self.root = root

    def __eq__(self, other):
        return isinstance(other, Vertex) and self.vertex == other.vertex

    def __hash__(self):
        return hash(self.vertex)

def primMST(graph: Graph, start_vertex: str = None):
    if graph.type == "Directed":
        print("Error: Graph is directed")
        return
    
    start_vertex = start_vertex if start_vertex else graph.get_vertices()[0]
    
    vertices = {v: Vertex(v) for v in graph.get_vertices()}
    vertices[start_vertex].key = 0
    
    ans = []

    while vertices:
        u = min(vertices.values(), key=lambda vertex: vertex.key)
        ans.append(u)
        del vertices[u.vertex]
        
        for v in graph.get_adjacent_vertices(u.vertex):
            if v in vertices:
                weight = graph.get_edge_weight(u.vertex, v)
                if weight < vertices[v].key:
                    vertices[v].key = weight
                    vertices[v].root = u.vertex
    
    mstGraph = Graph(directed=False)
    for vertex in graph.get_vertices():
        mstGraph.add_vertex(vertex)
    
    for vertex in ans:
        if vertex.root:
            mstGraph.add_edge(vertex.root, vertex.vertex, graph.get_edge_weight(vertex.root, vertex.vertex))
    
    return mstGraph
