from functions import *

if __name__ == "__main__":
    
    # Zadatak 1
    G = make_graph()
    print("Graph")
    print_graph(G)
    print()

    # Zadatak 2
    print("In deg:")
    in_degrees = get_in_degrees(G)
    for node in in_degrees:
        print(node + ":" + str(in_degrees[node]))

    print()
    print("Out deg:")
    out_degrees = get_out_degrees(G)
    for node in out_degrees:
        print(node + ":" + str(out_degrees[node]))

    print()

    # Zadatak 3
    path = shortest_path(G, "a", "g")

    print("Shortest path from a to g: ", end = "")
    
    for p in path[0]:
        print(p, end = " ")

    print()
    print("Length:", path[1])
    print()

    #Zadatak 4/5
    update_edge(G, "b", "c", -6)
    print("Added edge b -> c: -6")
    path = shortest_path(G, "a", "g")

    print("New shortest path from a to g: ", end = "")
    
    for p in path[0]:
        print(p, end = " ")

    print()
    print("Length:", path[1])    