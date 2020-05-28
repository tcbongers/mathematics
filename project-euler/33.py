num = 1
den = 1

def gcd(a, b):
	while b > 0:
		a, b = b, a % b
	return a
	
for a in range(10, 100):
	for b in range(a, 100):
		if '0' in str(a) or '0' in str(b):
			continue
		
		a_str = set(str(a))
		b_str = set(str(b))
		o = a_str & b_str
		
		if len(o) == 1 and len(a_str) == 2 and len(b_str) == 2:
			
			c = int((set(str(a)) - o).pop())
			d = int((set(str(b)) - o).pop())
		
			# a/b = c/d
			if d*a == b*c:
				print(f'{a}/{b} = {c}/{d}')
				num *= c
				den *= d
				
print(den // gcd(num, den))