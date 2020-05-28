import pickle
with open('primes_exponent_4', 'rb') as f:
	primes = pickle.load(f)
	
def is_prime(n, primes):
	for p in primes:
		
		if n % p == 0:
			return n == p
			
	return True
		
best = [-1000, 0]
max_count = 0
		
for a in range(-1000, 1000):
	print(a)
	for b in range(0, 1000):
		if 1 + a + b < 0:
			continue
		
		if b not in primes:
			continue
		
		prime_count = 0
		n = 0
		
		while True:
			if is_prime(n*n + a*n + b, primes):
				prime_count += 1
				n += 1
			else:
				break
			
		if prime_count > max_count:
			best = [a, b]
			print(best)
			max_count = prime_count
		
print(best, best[0]*best[1])