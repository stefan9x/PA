from functions import *

if __name__ == "__main__":
     G = MakeGraph()
     
     path = ShortestPath(G, G.nodes[0], G.nodes[3]) 

     print("----Graph----")
     PrintGraph(G)
     print()

     print("----Shortest Path----")
     print("From: " + G.nodes[0].ip + " to " + G.nodes[3].ip)
     print(path[0])
     print("Length:", path[1]) 

     print()
     print("----New paths after update----")
     UpdateEdge(G, G.nodes[0], G.nodes[3], 1)
     path = ShortestPath(G, G.nodes[0], G.nodes[3]) 
     print("----Shortest Path----")
     print("From: " + G.nodes[0].ip + " to " + G.nodes[3].ip)
     print(path[0])
     print("Length:", path[1]) 

     UpdateEdge(G, G.nodes[-3], G.nodes[-5], 1)

     path = ShortestPath(G, G.nodes[0], G.nodes[-1]) 
     print("----Shortest Path----")
     print("From: " + G.nodes[0].ip + " to " + G.nodes[-1].ip)
     print(path[0])
     print("Length:", path[1]) 

     print()
     print("----New graph after all changes----")
     PrintGraph(G)