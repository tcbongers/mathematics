size = 1001
cap = size // 2 + 2

s = 0


s += sum([(2*n - 1)*(2*n - 1) for n in range(1, cap)])
s += sum([4*n*n - 10*n + 7 for n in range(1, cap)])
s += sum([4*(n - 1)*(n - 1) + 1 for n in range(1, cap)])
s += sum([4*n*n - 6*n + 3 for n in range(1, cap)])
	
print(s - 3)