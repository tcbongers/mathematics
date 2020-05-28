# Generate all abundant numbers
def is_abundant(n):
	div_sum = 0
	
	d = 1
	while d*d < n:
		if n % d == 0:
			div_sum += d + n // d
		d += 1
	if n == d*d:
		div_sum += d
	
	return div_sum > 2*n
	
abund = list(filter(is_abundant, range(28123)))
sums = {}

for a in abund:
	for b in abund:
		if a + b > 28123:
			break
		if a + b in sums:
			continue
		else:
			sums[a + b] = 1
			
print((28123*28124) // 2 - sum(list(sums)))