from graph_vertex import *
from functions import *
import math
import time

if __name__ == "__main__":
    
    G = Graph()

    G.add_node("s", math.inf)
    G.add_node("t", math.inf)
    G.add_node("x", math.inf)
    G.add_node("y", math.inf)
    G.add_node("z", math.inf)

    G.add_edge("s", "t", 10)
    G.add_edge("s", "y", 5)

    G.add_edge("t", "x", 1)
    G.add_edge("t", "y", 2)

    G.add_edge("x", "z", 4)

    G.add_edge("y", "t", 3)
    G.add_edge("y", "x", 9)
    G.add_edge("y", "z", 2)

    G.add_edge("z", "x", 6)
    G.add_edge("z", "s", 7)

    dijkstra(G, "s")
    
    print("Graph 1")
    print_all_paths(G, "s")
    print_graph(G)
    
    print()
    print("Random graph")
    G1 = create_graph(5, 15, 20)

    s_p = random.choice(list(G1.nodes))
    dijkstra(G1, s_p)

    print_graph(G1)
    print_all_paths(G1, s_p)
    