from classes import *
from math import inf

def MakeGraph():
    
    G = Graph()

    G.addNode("192.168.242.10", inf)
    G.addNode("192.168.242.100", inf)
    G.addNode("192.168.242.95", inf)
    G.addNode("192.168.10.10", inf)
    G.addNode("192.168.242.35", inf)
    G.addNode("192.168.242.48", inf)
    G.addNode("192.168.242.102", inf)
    G.addNode("192.168.10.11", inf)
    G.addNode("192.168.242.73", inf)
    G.addNode("192.168.242.84", inf)

    G.addEdge("192.168.242.10", "192.168.242.100", 5)
    G.addEdge("192.168.242.10", "192.168.242.73", 3)

    G.addEdge("192.168.242.100", "192.168.242.95", 4)
    G.addEdge("192.168.242.100", "192.168.242.102", 3)

    G.addEdge("192.168.242.95", "192.168.242.84", 3)

    G.addEdge("192.168.10.10", "192.168.10.11", 1)

    G.addEdge("192.168.242.35", "192.168.242.102", 3)
    G.addEdge("192.168.242.35", "192.168.242.48", 1)

    G.addEdge("192.168.242.48", "192.168.242.84", 4)
    G.addEdge("192.168.242.48", "192.168.242.73", 1)

    G.addEdge("192.168.242.102", "192.168.242.84", 1)
    G.addEdge("192.168.242.102", "192.168.242.10", 1)

    G.addEdge("192.168.10.11", "192.168.10.10", 1)

    G.addEdge("192.168.242.73", "192.168.242.35", 4)

    G.addEdge("192.168.242.84", "192.168.242.100", 1)

    return G

def PrintGraph(G):
    for node in G.nodes:
        for dst in G.connections[node]:
            print(node + "(" + str(G.nodes[node]) + ") -> " + dst + "(" + str(G.nodes[dst]) + ") : " + str(G.weights[(node, dst)]))

def GetShortestPath(G, path, src, dst):
    if dst == src:
        path.append(src)
    elif G.parent[dst] == None:
        return None
    else:
        GetShortestPath(G, path, src, G.parent[dst])
        path.append(dst)

def ExtractMin(Q):
    m = list(Q.keys())[0]

    for node in Q:
        if Q[node] < Q[m]:
            m = node

    del Q[m]
    return m

def InitializeSingleSource(G, src):
    for node in G.nodes:
        G.nodes[node] = inf
        G.addParent(node, None)

    G.nodes[src] = 0

def Relax(G, src, dst):
    weight = G.weights[(src, dst)]

    if G.nodes[dst] > G.nodes[src] + weight:
        G.nodes[dst] = G.nodes[src] + weight
        G.addParent(dst, src)

def Dijkstra(G, src):
    InitializeSingleSource(G, src)
    
    Q = G.nodes.copy()

    while Q:
        m = ExtractMin(Q)
        for dst in G.connections[m]:
            Relax(G, m, dst)

def ShortestPath(G, src, dst):
    p = []
    path = ""

    Dijkstra(G, src)
    GetShortestPath(G, p, src, dst)

    for i in range (len(p)):
        if i == len(p)-1:
            path += p[i]
        else:
            path += p[i] + "->"

    if path != "":
        return [path, G.nodes[p[-1]]]
    else:
        return ["No route found", inf]

def UpdateEdge(G, src, dst, w):

    if dst not in G.connections[src]:
        G.addEdge(src, dst, w)
    else:
        G.weights[(src, dst)] = w