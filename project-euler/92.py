memo = {1:1, 89:89}

def ending(n):
	if n in memo:
		return memo[n]
		
	current = n
	chain = [n]
	
	while current != 1 and current != 89:
		current = sum([int(_)**2 for _ in str(current)])
		
		if current in memo:
			current = memo[current]
			break
			
		chain.append(current)
	
	for c in chain:
		memo[c] = current
		
	return current
		
count = 0
for k in range(1, 10**7):
	#print(k, ending(k))
	
	if ending(k) == 89:
		count += 1
		
print(count)