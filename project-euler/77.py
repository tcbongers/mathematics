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
	
	
memo = {}

def count_ways(target, coins):
	memo_string = str(target) + ' ' + str(len(coins))
	if memo_string in memo:
		return memo[memo_string]
		
	if target < 0:
		memo[memo_string] = 0
		return 0
	
	if target == 0:
		memo[memo_string] = 1
		return 1
	
	ways = 0
	for coin_index in range(len(coins)):
		ways += count_ways(target - coins[coin_index], coins[0:coin_index + 1])
		
	memo[memo_string] = ways
	return ways
	
coin_list = generate_primes(1000)
for k in range(200):
	print(f'Target {k}, number of ways = {count_ways(k, coin_list)}')
	if count_ways(k, coin_list) > 5000:
		break