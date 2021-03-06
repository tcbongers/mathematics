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
	
primes = generate_primes(1000)
for k in range(10**6):
	if unique_prime_factors(k, primes) == 4 and unique_prime_factors(k + 1, primes) == 4 and unique_prime_factors(k + 2, primes) == 4 and unique_prime_factors(k + 3, primes) == 4:
		print(f'{k} = {factor(k, primes)}')
		print(f'{k+1} = {factor(k+1, primes)}')
		print(f'{k+2} = {factor(k+2, primes)}')
		print(f'{k+3} = {factor(k+3, primes)}')
		break