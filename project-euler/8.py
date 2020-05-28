def product(number_array):
	out = 1
	for n in number_array:
		out *= int(n)
		
	return out
	
with open('8_data.txt') as f:
	lines = f.readlines()
	
	number_string = ''
	for line in lines:
		number_string += line
		if number_string[-1] == '\n':
			number_string = number_string[:-1]
			
	#print(number_string)
	
product_length = 13
max_product = 0

for start in range(0, len(number_string) - product_length):
	max_product = max(max_product, product(number_string[start:start + product_length]))
	
print(max_product)