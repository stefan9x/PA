from cls import *

def MakeGraph():

	G = Graph()
	G.nodes["a"] = Node("a")
	G.nodes["b"] = Node("b")
	G.nodes["c"] = Node("c")
	G.nodes["d"] = Node("d")
	G.nodes["e"] = Node("e")
	G.nodes["f"] = Node("f")

	G.nodes["a"].connection.append("b")
	G.nodes["a"].connection.append("d")

	G.nodes["b"].connection.append("e")

	G.nodes["c"].connection.append("e")
	G.nodes["c"].connection.append("f")

	G.nodes["d"].connection.append("b")

	G.nodes["e"].connection.append("d")

	G.nodes["f"].connection.append("f")

	return G

def PrintGraph(G):
	
	for n in G.nodes:
		print(G.nodes[n].name + ":", end = " ")
		for c in G.nodes[n].connection:
			print(c, end = "")
		print()

def PrintTimes(G):

	for n in G.nodes:
		print(n + ":" + str(G.nodes[n].ftime) + "/" + str(G.nodes[n].ltime))
	

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

	for n in G.nodes:
		nG.nodes[n] = Node(n)

	for n in G.nodes:
		for c in G.nodes[n].connection:
			nG.nodes[c].connection.append(n)

	return nG

def ApplyDFS(G):
	global time
	SCC = []
	for n in G.nodes:
		G.nodes[n].color = "WHITE"
		G.nodes[n].parent = None

	time = 0

	for n in G.nodes:
		if G.nodes[n].color == "WHITE":
			DFSVisit(G, n, SCC)

def DFSVisit(G, u, SCC):
	global time
	time = time + 1
	G.nodes[u].ftime = time
	G.nodes[u].color = "GRAY"
	SCC.append(u)
	
	for c in G.nodes[u].connection:
		if G.nodes[c].color == "WHITE":
			G.nodes[c].parent == u
			DFSVisit(G, c, SCC)

	G.nodes[u].color = "BLACK"
	time = time + 1
	G.nodes[u].ltime = time

def ApplyDFSInOrder(G, tG):
	
	L = []
	sortedG = []

	for n in G.nodes:
		L.append(G.nodes[n].ltime)

	L.sort(reverse = True)

	for t in L:
		for n in G.nodes:
			if G.nodes[n].ltime == t:
				sortedG.append(n)

	#DFS
	global time
	SCC = []

	for n in sortedG:
		tG.nodes[n].color = "WHITE"
		tG.nodes[n].parent = None

	time = 0

	for n in sortedG:
		if tG.nodes[n].color == "WHITE":
			DFSVisit(tG, n, SCC)
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
		