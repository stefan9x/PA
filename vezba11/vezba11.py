from functions import *

if __name__ == "__main__":
    # G[0] - Vertexes
    # G[1] - Edges
    # G[0][0] - first vertex in vertexes("a" in this case)
    # G[0][6] - last vertex in vertexes("g" in this case)

    
    # Zadatak 1
    G = make_graph()
    print_graph(G)

    # Zadatak 2
    print("In deg:")
    for v, deg in get_in_degrees(G):
        print(v, deg)

    print()
    print("Out deg:")
    for v, deg in get_out_degrees(G):
        print(v, deg)

    print()

    # Zadatak 3
    path = shortest_path(G, G[0][0], G[0][6])

    print("Shortest path from " + str(G[0][0]) + " to " + str(G[0][6]) + ":", end = "")
    
    for p in path[0]:
        print(p, end = " ")

    print()

    #Zadatak 4/5
    update_edge(G, G[0][1], G[0][2], -6)

    path = shortest_path(G, G[0][0], G[0][6])

    print("New shortest path from " + str(G[0][0]) + " to " + str(G[0][6]) + ":", end = "")
    
    for p in path[0]:
        print(p, end = " ")

    print()
    