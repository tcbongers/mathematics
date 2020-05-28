import bisect

def generate_primes(n):
	# Generate all the primes up to n
	
	primes = []
	
	testing_array = [1]*n
	testing_array[0] = 0
	testing_array[1] = 0
	
	#current_index = 2
	current_prime = 2
	
	while current_prime < n:
		primes.append(current_prime)
		
		running_index = 1
	
		while current_prime + current_prime * running_index < n:
			testing_array[current_prime + current_prime * running_index] = 0
			running_index += 1
			
		current_prime += 1
		while current_prime < n and testing_array[current_prime] == 0:
			current_prime += 1
	
	return primes
	
def factor(n, primes):
	
	# Return a factorization of the form [[prime, power]]
	prime_factors = []
	for p in primes:
		if p*p > n:
			if n > 1:
				prime_factors.append([n, 1])
			break
			
		if n % p == 0:
			exponent = 0
			while n % p == 0:
				exponent += 1
				n = n // p
			prime_factors.append([p, exponent])
			
	return prime_factors
	
def unique_prime_factors(n, primes):
	return len(factor(n, primes))
	
def num_factors(n, primes):
	factors = factor(n, primes)
	prod = 1
	
	for f in factors:
		prod *= (f[1] + 1)
		
	return prod
	
def euler_phi(n, primes):
	fs = factor(n, primes)
	phi = n
	
	for f in fs:
		p = f[0]
		n = (p - 1) * n // p
		
	return phi
	
def is_prime(n, primes):
	ind = bisect.bisect_left(primes, n)
	return(primes[ind] == n)

def is_left_trunc(p, primes):
	if p < 10:
		return 1
	t = int(str(p)[1:])
	
	if not is_prime(t, primes):
		return 0
		
	return is_left_trunc(t, primes)
	
def is_right_trunc(p, primes):
	if p < 10:
		return 1
		
	t = p // 10
	if not is_prime(t, primes):
		return 0
		
	return is_right_trunc(t, primes)
	
primes = generate_primes(10**6)
s, count = 0, 0

for p in primes:
	if p < 10:
		continue
		
	if is_left_trunc(p, primes) and is_right_trunc(p, primes):
		#print(p)
		count += 1
		s += p
		
print(f'The sum of the {count} truncatable primes is {s}')