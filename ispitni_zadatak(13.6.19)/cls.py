from collections import defaultdict

class Node():
	def __init__(self, n):
		self.name = n
		self.color = None
		self.connection = []
		self.parent = None
		self.ftime = None
		self.ltime = None

class Graph():
	def __init__(self):
		self.nodes = defaultdict(Node)