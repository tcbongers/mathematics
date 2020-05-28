""" 
	Library for doing operations with prime numbers. Includes methods
	for generating primes up to a given number, factoring based on those primes,
	and computing things such as the Euler phi function.
"""

def generate_primes(n):
	"""
	Use the seive of Erathosthenes to generate all the primes up to a cap, n
	"""
	
	# Initialize an array that has 1 in every coordinate
	# Any composite number gets set to zero eventually,
	# so the primes are the 1s that remain.
	
	primes = []
	testing_array = [1]*n
	testing_array[0] = 0
	testing_array[1] = 0
	
	# Algorithm: if the current index has not yet been marked composite,
	# mark all its multiples as composite and continue.
	# Keep primes in a separate array for safe keeping.
	
	current_prime = 2
	while current_prime < n:
		primes.append(current_prime)
		
		running_index = 1
	
		# Mark multiples as composite
		while current_prime + current_prime * running_index < n:
			testing_array[current_prime + current_prime * running_index] = 0
			running_index += 1
			
		current_prime += 1
		while current_prime < n and testing_array[current_prime] == 0:
			current_prime += 1
	
	return primes
	
def factor(n, primes):
	"""
		Factor n given the list of primes; run through each prime and check
		for divisibility; then append the correct power. Output has the form
		[[p, a_p] : p | n]
	"""
	
	prime_factors = []
	for p in primes:
		# Primes are now too large; if we haven't yet factored n, the leftover piece is prime.
		if p*p > n:
			if n > 1:
				prime_factors.append([n, 1])
			break
			
		# Division to pull off as many powers as possible
		if n % p == 0:
			exponent = 0
			while n % p == 0:
				exponent += 1
				n = n // p
			prime_factors.append([p, exponent])
			
	return prime_factors
	
def unique_prime_factors(n, primes):
	""" Count the number of prime factors of n """
	return len(factor(n, primes))
	
def num_factors(n, primes):
	""" Count the number of factors of n, including composites """
	
	factors = factor(n, primes)
	prod = 1
	
	for f in factors:
		prod *= (f[1] + 1)
		
	return prod
	
def euler_phi(n, primes):
	""" Compute the Euler phi function of n """
	fs = factor(n, primes)
	phi = n
	
	for f in fs:
		p = f[0]
		n = (p - 1) * n // p
		
	return phi
	
def save_primes(exponent):
	"""
		Generate all the primes up to 10^exp and dump them to a pickled
		file for later usage.
		
		To unpack: run the following after setting exponent variable:
		with open(f'primes_exponent_{exponent}', 'rb') as f: primes = pickle.load(f)
	"""
	import pickle
	primes = generate_primes(10**exponent)
	with open(f'primes_exponent_{exponent}', 'wb') as f:
		pickle.dump(primes, f)
