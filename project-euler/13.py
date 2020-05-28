with open('13_data.txt') as f:
	data_lines = f.readlines()
	numbers = [int(a[:-1]) for a in data_lines]
	print(str(sum(numbers))[0:10])