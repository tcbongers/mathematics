from math import log

with open('p099_base_exp.txt') as f:
	read_data = f.read()
	data_array = read_data.split('\n')
	bases = []
	exps = []
	
	for d in data_array:
		data_row = d.split(',')
		bases.append(int(data_row[0]))
		exps.append(int(data_row[1]))

max_power = 0
max_line = 0

for k in range(len(bases)):
	temp = exps[k]*log(bases[k])
	
	if temp > max_power:
		max_line, max_power = k + 1, temp 
	
print(f'Maximum value at line {max_line}')