from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = {}
        self.parent = {}
        self.connections = defaultdict(list)
        self.weight = {}

    def add_node(self, name, data):
        self.nodes[name] = data

    def add_edge(self, src, dst, w):
        self.connections[src].append(dst)
        self.weight[(src, dst)] = w

    def add_parent(self, node, parent):
        self.parent[node] = parent