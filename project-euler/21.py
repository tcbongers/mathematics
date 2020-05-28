def divisor_sum(n):
	s = 1
	k = 1
	while k*k < n:
		k += 1
		if n % k == 0:
			s += k + n // k
			
	if k*k == n:
		s += k
	
	return s
	
s = 0
	
for a in range(1, 10000):
	b = divisor_sum(a)
	if a != b and divisor_sum(b) == a:
		print(a, b)
		s += a + b
		
print(s // 2)