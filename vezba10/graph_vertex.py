from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = {}
        self.parent = {}
        self.edges = defaultdict(list)
        self.weight = {}

    def add_node(self, name, data):
        self.nodes[name] = data

    def add_edge(self, src, dst, w):
        self.edges[src].append(dst)
        self.weight[(src, dst)] = w

    def add_parent(self, node, parent):
        self.parent[node] = parent