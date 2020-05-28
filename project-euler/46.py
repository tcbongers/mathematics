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
			
squares = [n*n for n in range(100)]
primes = generate_primes(10**4)
odd_composite = 9
		
flag = True			
while flag:
	while odd_composite in primes:
		odd_composite += 2
		
	for p in primes:
		if p > odd_composite:
			print(f'Counterexample: {odd_composite}')
			flag = False
			break
			
		if (odd_composite - p) // 2 in squares:
			square_index = squares.index((odd_composite - p) // 2)
		#	print(f'{odd_composite} = {p} + 2 * {square_index}^2')
			break
			
	odd_composite += 2
	