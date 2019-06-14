import math
import random
import string
from graph_cls import *

def print_path(G, src, dst):
    if dst == src:
        print(src, end = " ")
    elif G.parent[dst] == None:
        print("No path from " + src + " to " + dst + " exist.", end = " ")
    else:
        print_path(G, src, G.parent[dst])
        print(dst, end = " ")

def print_all_paths(G, src):
    for node in G.nodes:
        print("Shortest path from " + src + " to " + node + ":", end = " ")
        print_path(G, src, node)
        print()

def print_graph(G):
    print()
    for node in G.nodes:
        for dst in G.connections[node]:
            print(node, end = " -> ")
            print(dst, end = " : ")
            print(G.weight[node, dst])
    
def dijkstra(G, src):
    init_single_src(G, src)
    S = []
    Q = G.nodes.copy()
    
    while Q:
        m = extract_min(Q)
        S.append(m)
        
        for dst in G.connections[m]:
            relax(G, m, dst)

def init_single_src(G, src):
    for node in G.nodes:
        G.nodes[node] = math.inf
        G.add_parent(node, None)

    G.nodes[src] = 0

def relax(G, src, dst):
    w = G.weight[(src, dst)]
    if G.nodes[dst] > G.nodes[src] + w:
        G.nodes[dst] = G.nodes[src] + w
        G.parent[dst] = src

def extract_min(N):
    m = list(N.keys())[0]

    for node in N:
        if N[node] < N[m]:
            m = node

    N.pop(m)
    return m

def create_graph(n_num, e_num, max_w):
    G = Graph()

    for n in range(n_num):
        if n_num < len(string.ascii_lowercase):
            G.add_node(string.ascii_lowercase[n], math.inf)
        else:
            G.add_node(str(n), math.inf)

    for e in range(e_num):
        src = random.choice(list(G.nodes))
        dst = random.choice(list(G.nodes))
        w = random.randint(0, max_w)
        
        cnt = 0
        
        while(True):
            if cnt == n_num:
                break

            if dst not in G.connections[src]:
                G.add_edge(src, dst, w)
                break
            else:
                dst = random.choice(list(G.nodes))
                cnt += 1
    return G