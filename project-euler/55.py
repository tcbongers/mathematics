def iteration_count(n):
	count = 1
	n = int(str(n)) + int(str(n)[::-1])
	
	while str(n) != str(n)[::-1]:
		n = int(str(n)) + int(str(n)[::-1])
		count += 1
	
		if count == 50:
			count = -1
			break
		
	return count
		
lychrel_count = 0

for k in range(10001):
	if iteration_count(k) == -1:
		print(k)
		lychrel_count += 1
		
print(lychrel_count)