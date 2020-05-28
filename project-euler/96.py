class Sudoku:
	
	def __init__(self, arr):
		self.data_table = arr
		self.options = self.generate_options()
		self.count = self.option_count()
		
		#print('generating')
		
	def __str__(self):
		string = '\n'
		
		for _ in range(9):
			row = ''.join(self.data_table[_])
			string += (row[0:3] + ' | ' + row[3:6] + ' | ' + row[6:] + '\n').translate({48:'_'})
			
			if _ == 2 or _ == 5:
				string += '---------------\n'
		return string
		
	def count_zeros(self):
		return sum([row.count('0') for row in self.data_table])
		
	def is_solved(self):
		return self.count_zeros() == 0
		
	def generate_options(self):
		options = []
		for row in range(9):
			options_row = []
			for col in range(9):
				if self.data_table[row][col] != '0':
					cell_options = [self.data_table[row][col]]
				else:
					cell_options= [_ for _ in '123456789']
					for r in range(9):
						if r == row:
							continue
						
						if self.data_table[r][col] in cell_options:
							cell_options.remove(self.data_table[r][col])
				
					for c in range(9):
						if c == col:
							continue
						
						if self.data_table[row][c] in cell_options:
							cell_options.remove(self.data_table[row][c])
							
					# Local 3 x 3 cell
					local_data = []
					for _ in range(3):
						local_data += self.data_table[3*(row//3) + _][3*(col//3):3*(col//3) + 3]
						for l in local_data:
							if l in cell_options:
								cell_options.remove(l)
								
						
				options_row.append(cell_options)
			options.append(options_row)
		
		return options
	
	def option_count(self):
		count = 1
		for cell in self.options:
			for _ in cell:
				count *= len(_)
		return count
		
	def solution_status(self):
		print(f'Remaining cells: {self.count_zeros()}')
		print(f'Number of options: {self.option_count()}')
		
	def update(self):
		for row in range(9):
			for col in range(9):
				if self.data_table[row][col] == '0' and len(self.options[row][col]) == 1:
					self.data_table[row][col] = self.options[row][col][0]
		self.options = self.generate_options()
		self.count = self.option_count()
					
with open('p096_sudoku.txt') as f:
	data = f.readlines()
	
tables = []
for row in range(len(data)):
	#print(type(data[row]))
	
	if data[row][0] == 'G':	# Get grid identifier
		current_table = []
		for _ in range(1, 10):
			table_row = data[row+_][:-1]	# Strip \n
			current_table.append([__ for __ in table_row])
			
		tables.append(current_table)
	
grid = Sudoku(tables[31])

last_option_count = 9**81
while not grid.is_solved():
	if grid.count == last_option_count:
		#grid.solution_status()
		break
		
	else:
		last_option_count = grid.count
		grid.update()
		
if grid.is_solved():
	print('Solved', grid)
else:
	print('Unsolved')
	grid.solution_status()