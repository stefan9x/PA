from collections import defaultdict   

class Graph:
    def __init__(self):
        self.nodes = {}
        self.connections = defaultdict(list)
        self.parent = {}
        self.weights = {}
        
    def addNode(self, name, data):
        self.nodes[name] = data

    def addEdge(self, src, dst, w):
        self.connections[src].append(dst)
        self.weights[(src, dst)] = w

    def addParent(self, node, parent):
        self.parent[node] = parent