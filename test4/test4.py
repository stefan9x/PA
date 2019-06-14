from functions import *

if __name__ == "__main__":
     
     G = MakeGraph()
     
     path = ShortestPath(G, "192.168.242.10", "192.168.10.10") 

     print("----Graph----")
     PrintGraph(G)
     print()

     print("----Shortest Path----")
     print("From: " + "192.168.242.10" + " to " + "192.168.10.10")
     print(path[0])
     print("Length:", path[1]) 

     print()
     print("----New paths after update----")
     UpdateEdge(G, "192.168.242.10", "192.168.10.10", 1)
     path = ShortestPath(G, "192.168.242.10", "192.168.10.10") 
     print("----Shortest Path----")
     print("From: " + "192.168.242.10" + " to " + "192.168.10.10")
     print(path[0])
     print("Length:", path[1]) 

     UpdateEdge(G, "192.168.10.11", "192.168.242.48", 1)

     path = ShortestPath(G, "192.168.242.10", "192.168.242.84") 
     print("----Shortest Path----")
     print("From: " + "192.168.242.10" + " to " + "192.168.242.84")
     print(path[0])
     print("Length:", path[1]) 

     print()
     print("----New graph after all changes----")
     PrintGraph(G)