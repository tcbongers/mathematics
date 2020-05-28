def count_children(row, col, a, b):
	# Count the number of a x b rectangles inside the parent
	# whose dimensions are row x col
	
	return (row + 1 - a)*(col + 1 - b)
	
def get_count(row, col):
	count = 0
	for a in range(1, row + 1):
		for b in range(1, col + 1):
			count += count_children(row, col, a, b)
	return count
	
	
best = 2*10**6
best_area = 0

for row in range(1, 100):
	for col in range(1, 100):
		if abs(get_count(row, col) - 2000000) < best:
			best_area = row*col
			best = abs(get_count(row, col) - 2000000)
			
print(f'Best area {best_area}, count {best}')