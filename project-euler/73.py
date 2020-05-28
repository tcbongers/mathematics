def gcd(a, b):
	while b > 0:
		a, b = b, a % b
	return a
	
cap = 12000
count = 0
	
for d in range(1, cap + 1):
	for n in range(d // 3 + 1, d // 2 + 1):
		#print(n, d)
		if gcd(d, n) == 1 and n*2 < d:
		#	print(f'{n}/{d}')
			count += 1
		
print(count)