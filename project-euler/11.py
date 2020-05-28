from functools import reduce

with open('p011_data.txt', 'r') as f:
	raw_data = f.readlines()
	
data = []
for row in raw_data:
	if row[-1] == '\n':
		data.append([int(a) for a in row[:-1].split(' ')])
	else:
		data.append([int(a) for a in row.split(' ')])
		
max_prod = 0	
mult = lambda x, y: x*y

for r in range(len(data)):
	for c in range(len(data[0]) - 3):
		current_data = data[r][c:c+4]
		max_prod = max(max_prod, reduce(mult, current_data))
		
for c in range(len(data[0])):
	for r in range(len(data) - 3):
		current_data = [data[r + k][c] for k in range(4)]
		max_prod = max(max_prod, reduce(mult, current_data))
		
for r in range(len(data[0]) - 3):
	for c in range(len(data) - 3):
		current_data = [data[r+k][c+k] for k in range(4)]
		max_prod = max(max_prod, reduce(mult, current_data))
		
for r in range(3, len(data[0])):
	for c in range(len(data) - 3):
		current_data = [data[r-k][c+k] for k in range(4)]
		max_prod = max(max_prod, reduce(mult, current_data))

print(max_prod)	