max_sum = 0

for a in range(1, 100):
	for b in range(1, 100):
		n = a**b
		max_sum = max(max_sum, sum([int(d) for d in str(n)]))
print(max_sum)