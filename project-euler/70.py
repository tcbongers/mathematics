import pickle
exp = 7
cap = 10**exp

factors = {n:{} for n in range(cap)}
factors[1] = {1:1}

current = 2

while current < cap:
	
	if factors[current] == {}:	# Found a prime, add to all multiples
		p = current
		k = 1
		while p*k < cap:
			factors[p*k][p] = 1
			k += 1
			
	elif len(factors[current]) == 1:	# Found a power of the prime
		p = list(factors[current].keys())[0]
		k = 1
		while current*k < cap:
			factors[current*k][p] += 1
			k += 1
	current += 1
	
def eulerPhi(n):
	phi = n
	f = factors[n]
	
	for p in f:
		phi = (phi*(p - 1)) // p
	return phi

best_n = 0
min_ratio = 10
for n in range(1, cap):
	phi = eulerPhi(n)
	if sorted(str(n)) == sorted(str(phi)):
		ratio = n / phi
		if ratio < min_ratio:
			print(n, phi, ratio, 'best')
			min_ratio = ratio
			best_n = n
		#else:
			#print(n, phi)
			
print(f'For cap 10^{exp}, minimum ratio at {best_n}')