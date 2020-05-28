def fact(n):
	if n == 0:
		return 1
	return n*fact(n - 1)
	
def choose(n, r):
	return fact(n) // (fact(n - r) * fact(r))
	
count = 0
	
for n in range(1, 101):
	for r in range(1, n + 1):
		if choose(n, r) > 10**6:
			count += 1
		
print(count)