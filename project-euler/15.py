# Answer is 40 choose 20

def fact(n):
	if n == 0:
		return 1
	
	return n*fact(n - 1)
	
print(fact(40) // (fact(20) * fact(20)))