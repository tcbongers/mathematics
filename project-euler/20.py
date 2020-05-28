def fact(n):
	if n == 1:
		return 1
	
	return n*fact(n - 1)
	
hundred_fact = fact(100)
print(sum([int(a) for a in str(hundred_fact)]))