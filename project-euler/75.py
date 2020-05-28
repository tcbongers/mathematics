def gcd(a, b):
	while b > 0:
		a, b = b, a % b
		
	return a
	
perim_count = {}
max_perim = 1500000

for n in range(1, max_perim, 2):
	if 2*n*n > max_perim:
		break
	
	for m in range(n + 2, max_perim, 2):
		
		if m*(m + n) > max_perim:
			break
			
		if gcd(n, m) > 1:
			continue
		g = 1
		while g*m*(m + n) < max_perim:
				
			perim = g*m*(m + n)
			if perim in perim_count:
				perim_count[perim] += 1
			else:
				perim_count[perim] = 1
			g += 1
			
goods = []
for p in perim_count:
	if perim_count[p] == 1:
		goods.append(p)
		
#print(sorted(goods))
		
print(f'{len(goods)} below {max_perim}')
#print(perim_count[108])