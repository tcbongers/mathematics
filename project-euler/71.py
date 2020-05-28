# The non-reduced fraction is always given by floor(3n/7) / n
# So we just need to reduce that

def gcd(a, b):
	while b > 0:
		a, b = b, a % b
	return a
	
cap = 10**6

best_fraction = [0, 1]
	
for denom in range(1, cap + 1):
	
	if 3*denom % 7 == 0:
		continue
	
	numerator = (3*denom) // 7
	fraction = [numerator // gcd(numerator, denom) , denom  // gcd(numerator, denom)]
	
	# Test if it's larger than the previous best
	if numerator*best_fraction[1] > denom*best_fraction[0]:
		best_fraction = fraction
	
print(best_fraction)