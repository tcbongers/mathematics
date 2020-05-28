import pickle
from bisect import bisect_left
from itertools import product

cap = 10000
with open('primes_exponent_8', 'rb') as f:
	primes = pickle.load(f)
small_primes = list(filter(lambda x : x < cap, primes))

print(f'Testing set: {len(primes)} primes')
print(f'{len(small_primes)} primes below {cap}')

pairs = []
for p in small_primes:
	for q in small_primes:
		if q < p:
			continue
			
		left = int(str(p) + str(q))
		right = int(str(q) + str(p))
		
		try:
			if primes[bisect_left(primes, left)] == left and primes[bisect_left(primes, right)] == right:
				pairs.append([p, q])
		except:
			continue
			
print(f'{len(pairs)} pairs')

triples = []
# Now look for triples by generating pairs with overlap
for a in pairs:
	for b in pairs:
		# Pairs are of the form (p, q) and (q, r)
		if a[1] == b[0]:
			#print(a, b)
			p = a[0]
			q = a[1]
			r = b[1]
			
			left = int(str(p) + str(r))
			right = int(str(r) + str(p))
		
			if [p, r] in pairs:
				triples.append([p, q, r])

#print(triples)				
print(f'{len(triples)} triples')

quads = []
# Now look for quadruples by taking triple + pair
#for a in triples:

for a in triples:
	p, q, r = a
	for b in triples:	# Look for form (p, q, r) and (q, r, s)
		q1, r1, s1 = b
		if q != q1 or r != r1:
			continue
			
		s = s1
		if [p, s] in pairs and [q, s] in pairs and [r, s] in pairs:
			quads.append(sorted([p, q, r, s]))
				
print(f'{len(quads)} quadruples: {quads}')

# Now look for five-tuples
found = False
for _ in quads:
	p, q, r, s = _
	
	for t in small_primes:
		if t <= s:
			continue
			
		if [p, t] in pairs and [q, t] in pairs and [r, t] in pairs and [s, t] in pairs:
			found = True
			print(p, q, r, s, t, '  sum',p + q + r + s + t)
			break
			
if not found:
	print(f'5-tuple not found below {cap}')