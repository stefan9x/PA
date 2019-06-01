class Node:
    def __init__(self, ip):
        self.ip = ip
        self.data = None
        self.parent = None

class Edge:
    def __init__(self, s, d, w):
        self.source = s
        self.destination = d
        self.weight = w

class Graph:
    def __init__(self, N, E):
        self.nodes = N
        self.edges = E        