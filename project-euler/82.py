class Node:
	def __init__(self, row, col, weight):
		self.row = row
		self.col = col
		self.weight = weight
		
		self.edges = []
		
	def __repr__(self):
		return f'Node ({self.row}, {self.col}) with weight {self.weight}'
		
	def __str__(self):
		return f'Node ({self.row}, {self.col}) with weight {self.weight}'
		
	def locate(self):
		return f'{self.row}_{self.col}'
		


data = [[131, 673, 234, 103, 18],
[201, 96, 342, 965, 150],
[630, 803, 746, 422, 111],
[537, 699, 497, 121, 956],
[805, 732, 524, 37, 331]]
f = open('p082_matrix.txt', 'r')
raw_data = f.readlines()

data = []
for r in raw_data:
	data.append([int(a) for a in r[:-1].split(',')])
# Initialize all nodes
start = Node(-1, -1, 0)
start.edges = [Node(_, 0, data[_][0]) for _ in range(len(data))]
nodes = [start]

node_grid = []
for row in range(len(data)):
	node_grid.append([Node(row, col, data[row][col]) for col in range(len(data[0]))])
	

for row in range(len(data)):
	for col in range(len(data[0])):
		n = node_grid[row][col]
		nodes.append(n)
		
		if row < len(data) - 1:
			n.edges += [Node(row + 1, col, data[row + 1][col])]
		if row > 0:
			n.edges += [Node(row - 1, col, data[row - 1][col])]
		if col < len(data) - 1:
			n.edges += [Node(row, col + 1, data[row][col + 1])]

current_node = start
distances = {}

for node in nodes:
	location = node.locate()
	distances[location] = 10**10

distances[start.locate()] = 0

while len(nodes) > 0:
	minimal_distance = 10**10
	for u in nodes:
		if distances[u.locate()] < minimal_distance:
			minimal_distance = distances[u.locate()]
			current_node = u
			
	nodes.remove(current_node)
	neighbors = current_node.edges
	
	for v in neighbors:
		alt = distances[current_node.locate()] + v.weight
		if alt < distances[v.locate()]:
			distances[v.locate()] = alt
	
minimum_distance = 10**10
for row in range(len(data)):
	
	target = f'{row}_{len(data[0]) - 1}'
	minimum_distance = min(minimum_distance, distances[target])
	#print(target, distances[target])
	
print(minimum_distance)