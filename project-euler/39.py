count = 0
perimeter_dictionary = {}

for a in range(1, 1000):
	print(a)
	for b in range(a + 1, 1000):
		if a + b > 1000:
			break
		
		for c in range(b + 1, 1000):
			
			p = a + b + c
			if p > 1000:
				break
			
			if a*a + b*b == c*c:
				if p in perimeter_dictionary:
					perimeter_dictionary[p] += 1
				else:
					perimeter_dictionary[p] = 1
				
#print(perimeter_dictionary[120])

max_perim = 0
max_count = 0

for p in perimeter_dictionary:
	if perimeter_dictionary[p] > max_count:
		max_perim = p
		max_count = perimeter_dictionary[p]
		
print(f'Maximum count = {max_count} at perimeter {max_perim}')