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
		n = ((p - 1) * n) // p
		
	return n
	
primes = generate_primes(2000)

cap = 10**6
s = 0

for d in range(1, cap + 1):
	#print(f'{d}, {euler_phi(d, primes)}')
	s += euler_phi(d, primes)
print(f'Cap = {cap}, count = {s - 1}')