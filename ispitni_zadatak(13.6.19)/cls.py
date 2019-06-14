from collections import defaultdict
from enum import Enum

class Graph:
	def __init__(self):
		self.nodes = []
		self.connections = defaultdict(list)
		self.parent = {}
		self.color = {}
		self.ftime = {}
		self.ltime = {}
        
	def addNode(self, name):
		self.nodes.append(name)

	def addEdge(self, src, dst):
		self.connections[src].append(dst)

	def addParent(self, node, parent):
		self.parent[node] = parent

class Color:
	BLACK = 0
	GRAY = 127
	WHITE = 255