def decimal_invert(n):
	rems = []
	num = 1
	denom = n
	
	while num < denom:
		num *= 10
	
	while True:
		div = num // denom
		rem = num % denom
		
		if rem == 0:
			return 0
	
		#print(div, rem)
		if rem in rems:
			return len(rems) - rems.index(rem)
		
		rems.append(rem)
		
		num = 10*rem
		
	return len(rems)
	
max_cycle = 0
for k in range(1, 1000):
	cycle = decimal_invert(k)
	if cycle > max_cycle:
		print(f'{k}, {cycle}')
		max_cycle = cycle
	