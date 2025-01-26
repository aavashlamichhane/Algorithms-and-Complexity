from graph import Graph

def kruskalMST(graph: Graph):
    
    if graph.type == "Directed":
        print("Error: Graph is directed")
        return
    ans = []
    sets = []
    for vertex in graph.get_vertices():
        sets.append({vertex})
    
    edges = sorted(graph.get_edges(), key=lambda tup: tup[2])
    
    for edge in edges:
        u, v, w = edge
        u_set = None
        v_set = None
        for s in sets:
            if u in s:
                u_set = s
            if v in s:
                v_set = s
        if u_set != v_set:
            ans.append(edge)
            sets.remove(u_set)
            sets.remove(v_set)
            sets.append(u_set.union(v_set))
    
    mstGraph = Graph(directed=False)
    for vertex in graph.get_vertices():
        mstGraph.add_vertex(vertex)
    
    for edge in ans:
        u, v, w = edge
        mstGraph.add_edge(u, v, w)
    
    return mstGraph

