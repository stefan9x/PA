import math
import random
from graph_vertex import *

def get_weight(E, s, d):
    for e in E:
        if e.source == s and e.destination == d:
            return e.weight

def extract_min(V):
    m = V[0]
    
    for v in V:
        if v.data < m.data:
            m = v

    V.remove(m)
    return m

def get_n(E, u):
    N = []
    
    for e in E:
        if e.source == u:
            N.append(e.destination)

    return N

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

def dijkstra(G, s):
    init_single_src(G[0], s)
    S = []
    Q = G[0][:]
    
    while Q:
        u = extract_min(Q)
        S.append(u)
        
        for v in get_n(G[1], u):
            relax(G[1], u, v)

def create_graph(v_num, e_num, max_w):
    V = []
    for v in range(v_num):
        V.append(Vertex(str(v), v))

    E = []
    for e in range(e_num):
        s = random.randint(0, v_num - 1)
        d = random.randint(0, v_num - 1)
        w = random.randint(0, max_w)
        
        test = Edge(V[s], V[d], w)
        
        found = False
        for e_t in E:
            if test.source == e_t.source and test.destination == e_t.destination:
                found = True

        if found == False:
            E.append(test)

    G = [V, E]
    
    return G