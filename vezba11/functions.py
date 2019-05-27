import math
import random
from graph_vertex import *

def make_graph():

    a = Vertex(n = "a")
    b = Vertex(n = "b")
    c = Vertex(n = "c")
    d = Vertex(n = "d")
    e = Vertex(n = "e")
    f = Vertex(n = "f")
    g = Vertex(n = "g")

    V = [a, b, c, d, e, f, g]

    E = []

    E.append(Edge(a, b, 8))
    E.append(Edge(a, c, 6))
    E.append(Edge(b, d, 10))
    E.append(Edge(c, d, 15))
    E.append(Edge(c, e, 9))
    E.append(Edge(d, e, 14))
    E.append(Edge(d, f, 4))
    E.append(Edge(e, f, 13))
    E.append(Edge(e, g, 17))
    E.append(Edge(f, g, 7))

    return [V, E]

def get_weight(E, s, d):
    for e in E:
        if e.source == s and e.destination == d:
            return e.weight

def print_path(s, d):
    if d == s:
        print(s, end = " ")
    elif d.parent == None:
        print("No path from " + str(s.name) + " to " + str(d.name) + " exist.", end = " ")
    else:
        print_path(s, d.parent)
        print(d, end = " ")

def print_all_paths(G, s):
    for v in G[0]:
        print("Shortest path from " + s.name + " to " + v.name + ":", end = " ")
        print_path(s, v)
        print()

def print_graph(G):
    print()
    for v in G[0]:
        for e in G[1]:
            if v == e.source:
                print(e.source, end = " -> ")
                print(e.destination, end = " : ")
                print(e.weight)
        print()

def find_path(s, d, path_list):
    if d == s:
        path_list.append(s)
    elif d.parent == None:
        return None
    else:
        find_path(s, d.parent, path_list)
        path_list.append(d)

def init_single_src(V, s):
    for v in V:
        v.data = math.inf
        v.parent = None

    s.data = 0

def relax(E, u, v):
    w = get_weight(E, u, v)
    if v.data > u.data + w:
        v.data = u.data + w
        v.parent = u

def bellman_ford(G, s):
    init_single_src(G[0], s)

    for i in range(len(G[0])):
        for e in G[1]:
            relax(G[1], e.source, e.destination)

    for e in G[1]:
        if e.destination.data > e.source.data + get_weight(G[1], e.source, e.destination):
            return False

    return True

def get_in_degrees(G):
    L = []

    for v in G[0]:
        deg = 0

        for e in G[1]:
            if e.destination == v:
                deg += 1

        L.append([v, deg])

    return L

def get_out_degrees(G):
    L = []

    for v in G[0]:
        deg = 0

        for e in G[1]:
            if e.source == v:
                deg += 1

        L.append([v, deg])

    return L

def shortest_path(G, s, d):
    path_list = []
    
    bellman_ford(G, s)
    find_path(s, d, path_list)

    #1 return list of vertexes in path
    #2 return total path length, stored in last vertex in path_list
    return [path_list, path_list[-1].data]

def update_edge(G, s, d, w):
    found = False
    
    for e in G[1]:
        if e.source == s and e.destination == d:
            e.weight = w
            found = True

    if not found:
        G[1].append(Edge(s, d, w))