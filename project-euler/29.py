cap = 100
powers = []

for a in range(2, cap + 1):
	for b in range(2, cap + 1):
		powers.append(a**b)
	
print(f'Number of distinct powers = {len(set(powers))}')