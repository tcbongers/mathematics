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
	
# If n is 9-pandigital, its digital sum is 45, divisible by 3
# If n is 8-pandigital, its digital sum is 36, divisible by 3
# So look for 7-pandigital
	
primes = generate_primes(2768)			
N = 7654321

while True:
	if set(str(N)) == set([str(a) for a in range(1, 8)]):
		if len(factor(N, primes)) == 1:
			print(N)
			break
	N -= 1