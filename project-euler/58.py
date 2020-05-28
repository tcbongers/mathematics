import pickle, bisect
with open('primes_exponent_5', 'rb') as f:
	primes = pickle.load(f)
	
def isPrime(n):
	for p in primes:
		if n < 2:
			return 0
			
		if n == p:
			return 1
			
		if n % p == 0 and n > p:
			return 0
	return 1
	
	
prime_count, count = 0, -3

for n in range(1, 10**5):
	count += 4
	size = 2*n - 1
	
	tests = [4*n*n - 10*n + 7, 4*(n - 1)*(n - 1) + 1, 4*n*n - 6*n + 3]
	for t in tests:
		#if isPrime(t):
		#	print(t)
		prime_count += isPrime(t)
			
			
	print(f'{n} -- Size {size} -- {prime_count}/{count} -- density={prime_count/count}')
	if prime_count > 0 and 10*prime_count < count:
		break