import math
import random
from graph_cls import *

def make_graph():

    G = Graph()
    
    G.add_node("a", math.inf)
    G.add_node("b", math.inf)
    G.add_node("c", math.inf)
    G.add_node("d", math.inf)
    G.add_node("e", math.inf)
    G.add_node("f", math.inf)
    G.add_node("g", math.inf)

    G.add_edge("a", "b", 8)
    G.add_edge("a", "c", 6)
    G.add_edge("b", "d", 10)
    G.add_edge("c", "d", 15)
    G.add_edge("c", "e", 9)
    G.add_edge("d", "e", 14)
    G.add_edge("d", "f", 4)
    G.add_edge("e", "f", 13)
    G.add_edge("e", "g", 17)
    G.add_edge("f", "g", 7)

    return G

def print_path(G, src, dst):
    if dst == src:
        print(src, end = " ")
    elif dst.parent == None:
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
    for node in G.nodes:
        for dst in G.connections[node]:
            print(node, end = " -> ")
            print(dst, end = " : ")
            print(G.weights[(node, dst)])

def find_path(G, src, dst, path_list):
    if dst == src:
        path_list.append(src)
    elif G.parent[dst] == None:
        return None
    else:
        find_path(G, src, G.parent[dst], path_list)
        path_list.append(dst)

def init_single_src(G, src):
    for node in G.nodes:
        G.nodes[node] = math.inf
        G.add_parent(node, None)

    G.nodes[src] = 0

def relax(G, src, dst):
    w = G.weights[(src, dst)]
    if G.nodes[dst] > G.nodes[src] + w:
        G.nodes[dst] = G.nodes[src] + w
        G.add_parent(dst, src)

def bellman_ford(G, src):
    init_single_src(G, src)

    for node in G.nodes:
        for dst in G.connections[node]:
            relax(G, node, dst)

    for node in G.nodes:
        for dst in G.connections[node]:
            if G.nodes[dst] > G.nodes[node] + G.weights[(node, dst)]:
                return False

    return True

def get_in_degrees(G):
    L = {}

    for node in G.nodes:
        deg = 0
        for node2 in G.nodes:
            for dst in G.connections[node2]:
                if dst == node:
                    deg += 1

        L[node] = deg

    return L

def get_out_degrees(G):
    L = {}

    for node in G.nodes:
        L[node] = len(G.connections[node])

    return L

def shortest_path(G, src, dst):
    path_list = []
    
    bellman_ford(G, src)
    find_path(G, src, dst, path_list)

    #1 return list of vertexes in path
    #2 return total path length, stored in last vertex in path_list
    return [path_list, G.nodes[path_list[-1]]]

def update_edge(G, src, dst, w):
    
    if dst not in G.connections[src]:
        G.add_edge(src, dst, w)
    else:
        G.weights[(src, dst)] = w