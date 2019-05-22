from vertex import *
from funs import *

if __name__ == "__main__":
    
    undershorts = Vertex(n = "undershorts")
    socks = Vertex(n = "socks")
    watch = Vertex(n = "watch")
    pants = Vertex(n = "pants")
    shoes = Vertex(n = "shoes")
    shirt = Vertex(n = "shirt")
    belt = Vertex(n = "belt")
    tie = Vertex(n = "tie")
    jacket = Vertex(n = "jacket")

    undershorts.connection = [pants, shoes]
    socks.connection = [shoes]
    watch.connection = []
    pants.connection = [belt, shoes]
    shoes.connection = []  
    shirt.connection = [belt, tie]
    belt.connection = [jacket]
    tie.connection = [jacket]
    jacket.connection = []

    G = [jacket, tie, belt, shirt, watch, shoes, pants, undershorts, socks]
    L = topological_sort(G)
    for l in reversed(L):
        print(l.name + "(" + str(l.data) + "/" + str(l.time) + ")")
    