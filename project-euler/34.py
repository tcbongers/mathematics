def fact(n):
	if n == 0:
		return 1
	return n*fact(n - 1)
	
facts = [fact(n) for n in range(10)]
	
# Given an n digit number, the sum of factorials
# is bounded by n*9!, while the number is at least
# 10^(n - 1). So we have n*9! >= 10^(n - 1)

# 3628800n > 10^n --> At most 7 digits

s = -3
for k in range(10**7):
	if sum([facts[int(d)] for d in str(k)]) == k:
		s += k
		print(k)
		
print(s)