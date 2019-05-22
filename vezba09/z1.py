from vertex import *
from funs import *

if __name__ == "__main__":
    
    # Graph 1
    G = []
    
    for i in range(5):
        G.append(Vertex(n=str(i+1), d=i+1))

    G[0].connection.append(G[1])
    G[0].connection.append(G[4])

    G[1].connection.append(G[0])
    G[1].connection.append(G[4])
    G[1].connection.append(G[3])
    G[1].connection.append(G[2])
    
    G[2].connection.append(G[1])
    G[2].connection.append(G[3])

    G[3].connection.append(G[4])
    G[3].connection.append(G[1])
    G[3].connection.append(G[2])

    G[4].connection.append(G[0])
    G[4].connection.append(G[1])
    G[4].connection.append(G[3])

    print_n_of_n(G[1])

    #Graph 2
    print("--G2--")

    G2 = []
    
    for i in range(6):
        G2.append(Vertex(n=str(i+1), d=i+1))

    G2[0].connection.append(G2[1])
    G2[0].connection.append(G2[3])

    G2[1].connection.append(G2[4])
    
    G2[2].connection.append(G2[4])
    G2[2].connection.append(G2[5])

    G2[3].connection.append(G2[1])

    G2[4].connection.append(G2[3])

    G2[5].connection.append(G2[5])

    print_n_of_n(G2[1])