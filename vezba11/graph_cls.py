from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = {}
        self.connections = defaultdict(list)
        self.parent = {}
        self.weights = {}
        
    def add_node(self, name, data):
        self.nodes[name] = data

    def add_edge(self, src, dst, w):
        self.connections[src].append(dst)
        self.weights[(src, dst)] = w

    def add_parent(self, node, parent):
        self.parent[node] = parent