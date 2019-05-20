from graph_vertex import *
from functions import *
import math

if __name__ == "__main__":
    
    s = Vertex("s", 0)
    t = Vertex("t", math.inf)
    x = Vertex("x", math.inf)
    y = Vertex("y", math.inf)
    z = Vertex("z", math.inf)

    V = []
    V = [s, t, x, y, z]
    
    E = []
    
    E.append(Edge(s, t, 10))
    E.append(Edge(s, y, 5))
    
    E.append(Edge(t, x, 1))
    E.append(Edge(t, y, 2))

    E.append(Edge(x, z, 4))
    
    E.append(Edge(y, t, 3))
    E.append(Edge(y, x, 9))
    E.append(Edge(y, z, 2))

    E.append(Edge(z, x, 6))
    E.append(Edge(z, s, 7))

    G = []

    G = [V, E]
    
    dijkstra(G, s)
    
    print("Graph 1")
    print_all_paths(G, s)

    print()
    print("Random graph")
    G1 = create_graph(5, 15, 20)

    s_p = G1[0][random.randint(0, 4)]

    dijkstra(G1, s_p)
    
    print_all_paths(G1, s_p)

    print_graph(G1)
    
    