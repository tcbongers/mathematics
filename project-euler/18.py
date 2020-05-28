triangle_data = []
costs = []

with open('18_data.txt') as f:
	raw_data = f.readlines()
	for row in raw_data:
		if row[-1] == '\n':
			row = row[:-1]
			
		triangle_data.append([int(col) for col in row.split(' ')])
		costs.append([0]*len(triangle_data[-1]))
			
costs[0][0] = triangle_data[0][0]

for row_index in range(len(triangle_data)):
	costs[row_index][0] = triangle_data[row_index][0] + costs[row_index - 1][0]
							
	costs[row_index][row_index] = triangle_data[row_index][row_index] + costs[row_index - 1][row_index - 1]
	
	for col_index in range(1, row_index):
		costs[row_index][col_index] = triangle_data[row_index][col_index] + max(costs[row_index - 1][col_index - 1], costs[row_index - 1][col_index])
	
#print(costs)
print(f'Maximum cost = {max(costs[-1])}')
