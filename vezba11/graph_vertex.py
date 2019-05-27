class Vertex:
    def __init__(self, n = None, d = None, p = None):
        self.name = n        
        self.data = d
        self.parent = p

    def __str__(self):
        return self.name + "(" + str(self.data) + ")"

class Edge:
    def __init__(self, s = None, d = None, w = None):
        self.source = s
        self.destination = d
        self.weight = w
        


