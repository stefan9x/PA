from cls import *

def MakeGraph():

	G = Graph()
	G.addNode("a")
	G.addNode("b")
	G.addNode("c")
	G.addNode("d")
	G.addNode("e")
	G.addNode("f")

	G.addEdge("a", "b")
	G.addEdge("a", "d")

	G.addEdge("b", "e")

	G.addEdge("c", "e")
	G.addEdge("c", "f")

	G.addEdge("d", "b")

	G.addEdge("e", "d")

	G.addEdge("f", "f")

	return G

def PrintGraph(G):
	
	for node in G.nodes:
		print(node + ":", end = " ")
		for conn in G.connections[node]:
			print(conn, end = "")
		print()

def PrintTimes(G):

	for node in G.nodes:
		print(node + ":" + str(G.ftime[node]) + "/" + str(G.ltime[node]))
	
def ApplyStrongConnectedComponents():

	G = MakeGraph()

	print("Graph")
	PrintGraph(G)
	ApplyDFS(G)
	print()

	print("Graph times")
	PrintTimes(G)
	print()

	trasposedG = TransposeGraph(G)
	print("Transposed Graph")
	PrintGraph(trasposedG)
	print()

	SCC = ApplyDFSInOrder(G, trasposedG)

	PrintStronglyConnectedComponents(SCC)

def TransposeGraph(G):
	nG = Graph()

	for node in G.nodes:
		nG.addNode(node)
		for conn in G.connections[node]:
			nG.addEdge(conn, node)

	return nG

def ApplyDFS(G):
	global time
	SCC = []
	for node in G.nodes:
		G.color[node] = Color.WHITE
		G.addParent(node, None)

	time = 0

	for node in G.nodes:
		if G.color[node] == Color.WHITE:
			DFSVisit(G, node, SCC)

def DFSVisit(G, u, SCC):
	global time
	time = time + 1
	G.ftime[u] = time
	G.color[u] = Color.GRAY
	SCC.append(u)
	
	for conn in G.connections[u]:
		if G.color[conn] == Color.WHITE:
			G.addParent(conn, u)
			DFSVisit(G, conn, SCC)

	G.color[u] = Color.BLACK
	time = time + 1
	G.ltime[u] = time

def ApplyDFSInOrder(G, tG):
	
	L = []
	sortedG = []

	for node in G.nodes:
		L.append(G.ltime[node])

	L.sort(reverse = True)

	for t in L:
		for node in G.nodes:
			if G.ltime[node] == t:
				sortedG.append(node)

	#DFS
	global time
	SCC = []

	for node in sortedG:
		tG.color[node] = Color.WHITE
		tG.addParent(node, None)

	time = 0

	for node in sortedG:
		if tG.color[node] == Color.WHITE:
			DFSVisit(tG, node, SCC)
			SCC.append(";")
	
	print("Sorted first graph:", end = " ")
	print(sortedG)
	print()
	
	print("Transposed graph times")
	PrintTimes(tG)
	print()

	return SCC

def PrintStronglyConnectedComponents(SCC):
	print("SCC:")
	
	for c in SCC:
		if c == ";":
			print()
		else:
			print(c, end = "")
		