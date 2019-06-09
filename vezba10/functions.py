import math
import random
import string
from graph_vertex import *

def print_path(G, s, d):
    if G.nodes[d] == G.nodes[s]:
        print(s, end = " ")
    elif G.parent[d] == None:
        print("No path from " + s + " to " + d + " exist.", end = " ")
    else:
        print_path(G, s, G.parent[d])
        print(d, end = " ")

def print_all_paths(G, s):
    for n in G.nodes:
        print("Shortest path from " + s + " to " + n + ":", end = " ")
        print_path(G, s, n)
        print()

def print_graph(G):
    print()
    for n in G.nodes:
        for e in G.edges[n]:
            print(n, end = " -> ")
            print(e, end = " : ")
            print(G.weight[n, e])
    
def dijkstra(G, s):
    init_single_src(G, s)
    S = []
    Q = G.nodes.copy()
    
    while Q:
        u = extract_min(Q)
        S.append(u)
        
        for n in G.edges[u]:
            relax(G, u, n)

def init_single_src(G, s):
    for g in G.nodes:
        G.nodes[g] = math.inf
        G.parent[g] = None

    G.nodes[s] = 0

def relax(G, u, v):
    w = G.weight[(u, v)]
    if G.nodes[v] > G.nodes[u] + w:
        G.nodes[v] = G.nodes[u] + w
        G.parent[v] = u

def extract_min(N):
    m = list(N.keys())[0]

    for v in N:
        if N[v] < N[m]:
            m = v

    N.pop(m)
    return m

def create_graph(v_num, e_num, max_w):
    G = Graph()

    for v in range(v_num):
        if v_num < len(string.ascii_lowercase):
            G.add_node(string.ascii_lowercase[v], math.inf)
        else:
            G.add_node(str(v), math.inf)

    for e in range(e_num):
        s = random.choice(list(G.nodes))
        d = random.choice(list(G.nodes))
        w = random.randint(0, max_w)
        
        cnt = 0
        
        while(True):
            if cnt == v_num:
                break

            if d not in G.edges[s]:
                G.add_edge(s, d, w)
                break
            else:
                d = random.choice(list(G.nodes))
                cnt += 1
    return G