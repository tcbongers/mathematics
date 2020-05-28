class Node:
	def __init__(self, row, col, weight=0):
		self.row = row
		self.col = col
		self.weight = weight
		
	def __str__(self):
		return f'({self.row}, {self.col})'
		
	def __repr__(self):
		return f'({self.row}, {self.col})'
		
class Edge:
	def __init__(self, start, end, cost=0):
		self.start = start
		self.end = end
		self.cost = cost
	
	def __str__(self):
		return(f'Cost {self.cost} on Edge {self.start} --> {self.end}')
	
f = open('p081_matrix.txt', 'r')
raw_data = f.readlines()

data = []
for r in raw_data:
	data.append([int(a) for a in r[:-1].split(',')])

#data = [[131, 673, 234, 103, 18],
#[201, 96, 342, 965, 150],
#[630, 803, 746, 422, 111],
#[537, 699, 497, 121, 956],
#[805, 732, 524, 37, 331]]

#costs = []
#for row in range(len(data)):
#	costs.append([0]*len(data[0]))
	
#costs[0][0] = data[0][0]
#for col in range(1, len(data[0])):
#	costs[0][col] = data[0][col] + costs[0][col-1]
	
#print(costs[0])
#for row in range(1, len(data)):
#	costs[row][0] = data[row][0] + costs[row-1][0]
#	for col in range(1, len(data[0])):
#		costs[row][col] = data[row][col] + min(costs[row-1][col], costs[row][col-1])
		
#print(costs[-1][-1])

# Build an adjacency dictionary; 
# nodes are given by 'row'_'col'
# edges are given by 'node'__'node'

nodes = [Node(row, col, data[row][col]) for row in range(len(data)) for col in range(len(data[0]))]
edges = []
adjacency = {}

# Internal data from the graph structure
for n in nodes:
	
	neighbors = []
	for m in nodes:
		if m.row == n.row + 1 and m.col == n.col:
			edges.append(Edge(n, m, m.weight))
			neighbors.append(m)
		if m.row == n.row and m.col == n.col + 1:
			edges.append(Edge(n, m, m.weight))
			neighbors.append(m)
	adjacency[n] = neighbors
			
# Initiate a starting node:
start = Node(-1, -1, data[0][0])
finish = Node(len(data), len(data[0]), data[-1][-1])
adjacency[start] = nodes[0]

nodes.append(start)
nodes.append(finish)

adjacency[nodes[-3]].append(finish)

edges.append(Edge(start, nodes[0], nodes[0].weight))
edges.append(Edge(nodes[-3], finish))

distances = {node:10**10 for node in nodes}
unvisited_nodes = nodes
distances[start] = 0
current_node = start

while len(unvisited_nodes) > 0:
	unvisited_nodes.remove(current_node)

	# Loop over neighbors
	for e in edges:
		if e.start == current_node:
			alt = distances[current_node] + e.cost
			if alt < distances[e.end]:
				distances[e.end] = alt
				
	# Set current node to be the closest one in
	min_cost = 10**10
	for n in unvisited_nodes:
		if distances[n] < min_cost:
			min_cost = distances[n]
			current_node = n
			
print(distances[finish])