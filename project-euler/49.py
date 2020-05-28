import pickle

with open('primes_exponent_4', 'rb') as f:
	primes = pickle.load(f)
	
primes = list(filter(lambda x : x > 1000, primes))

for p in range(len(primes)):
	for q in range(p + 1, len(primes)):
		p_1 = primes[p]
		q_1 = primes[q]
		
		if set(str(p_1)) == set(str(q_1)):
			#print(p_1, q_1)
			r_1 = 2*primes[q]  - primes[p]
			if r_1 in primes and set(str(r_1)) == set(str(p_1)):
				print(p_1, q_1, r_1)
				