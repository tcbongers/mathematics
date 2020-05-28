memo = {0:1}

def partition(n):
	# Compute the partition function p(n) using the pentagonal number
	# recurrence relation
	# p(n) = p(n - 1) + p(n - 2) - p(n - 5) - p(n - 7) + p(n - 12) + p(n - 15) - ...
	# with memoization.
	
	if n in memo:
		return memo[n]
	
	#if n == 0:
	#	return 1
	
	if n < 0:
		return 0
	
	p = 0
	# Run through positive k first

	k = 1
	while n - (3*k*k - k) // 2 >= 0:
		p += (-1)**(k + 1) * partition(n - (3*k*k - k) // 2)
		k += 1
	
	k = -1 
	while n - (3*k*k - k) // 2 >= 0:
		p += (-1)**(abs(k) + 1) * partition(n - (3*k*k - k) // 2)
		k -= 1
	
	memo[n] = p % 10**6
	return memo[n] 
	
for n in range(100001):
	if partition(n) == 0:
		print(n)
		break
		
	#print(n, partition(n))