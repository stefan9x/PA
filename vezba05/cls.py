class Node:
    def __init__(self, p = None, l = None, r = None, d = None):
        self.parent = p
        self.left = l
        self.right = r
        self.data = d

    def __str__(self):
        if self.data == None:
            return "None"
        else:
            return str(self.data.a1)

class Data:
    def __init__(self, val1, val2):
        self.a1 = val1
        self.a2 = val2