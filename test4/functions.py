from classes import *
from math import inf

def MakeGraph():
    
    E = []

    a = Node("192.168.242.10")
    b = Node("192.168.242.100")
    c = Node("192.168.242.95")
    d = Node("192.168.10.10")
    e = Node("192.168.242.35")
    f = Node("192.168.242.48")
    g = Node("192.168.242.102")
    h = Node("192.168.10.11")
    i = Node("192.168.242.73")
    j = Node("192.168.242.84")

    N=[a, b, c, d, e, f, g, h, i, j]

    E.append(Edge(a, b, 5))
    E.append(Edge(a, i, 3))

    E.append(Edge(b, c, 4))
    E.append(Edge(b, g, 3))

    E.append(Edge(c, j, 3))

    E.append(Edge(d, h, 1))

    E.append(Edge(e, g, 3))
    E.append(Edge(e, f, 1))

    E.append(Edge(f, j, 4))
    E.append(Edge(f, i, 1))

    E.append(Edge(g, j, 1))
    E.append(Edge(g, a, 1))

    E.append(Edge(h, d, 1))

    E.append(Edge(i, e, 4))

    E.append(Edge(j, b, 1))

    return Graph(N, E)

def PrintGraph(G):
    for n in G.nodes:
        for e in G.edges:
            if n == e.source:
                print(n.ip + "(" + str(n.data) + ")" + " -> " + e.destination.ip + "(" + str(n.data) + ")" + " : " + str(e.weight))

def GetShortestPath(G, path, s, d):
    if d == s:
        path.append(s)
    elif d.parent == None:
        return None
    else:
        GetShortestPath(G, path, s, d.parent)
        path.append(d)

def GetWeight(G, s, d):
    for e in G.edges:
        if e.source == s and e.destination == d:
            return e.weight

def ExtractMin(Q):
    m = Q[0]

    for n in Q:
        if n.data < m.data:
            m = n

    Q.remove(m)
    return m

def GetN(G, n):
    L = []

    for e in G.edges:
        if e.source == n:
            L.append(e.destination)

    return L

def InitializeSingleSource(G, s):
    for n in G.nodes:
        n.data = inf
        n.parent = None
    s.data = 0

def Relax(G, u, v):
    weight = GetWeight(G, u, v)

    if v.data > u.data + weight:
        v.data = u.data + weight
        v.parent = u

def Dijkstra(G, s):
    InitializeSingleSource(G, s)
    
    Q = G.nodes[:]

    while Q:
        u = ExtractMin(Q)
        for n in GetN(G, u):
            Relax(G, u, n)

def ShortestPath(G, s, d):
    p = []
    path = ""

    Dijkstra(G, s)
    GetShortestPath(G, p, s, d)

    for i in range (len(p)):
        if i == len(p)-1:
            path += p[i].ip
        else:
            path += p[i].ip + "->"

    if path != "":
        return [path, p[-1].data]
    else:
        return ["No route found", inf]

    

def UpdateEdge(G, s, d, w):

    found = False
    for e in G.edges:
        if e.source == s and e.destination == d:
            found = True
            e.weight = w

    if not found:
        G.edges.append(Edge(s, d, w))