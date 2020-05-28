import pickle
with open('primes_exponent_6', 'rb') as f:
	primes = pickle.load(f)

def keep(p):
	if p < 10:
		return 1
		
	if len(set(str(p)) & set('024568')) > 0:
		return 0
		
	return 1
	
print(f'Initial length: {len(primes)}')
filtered_primes = list(filter(keep, primes))
print(f'Filtered length: {len(filtered_primes)}')

circle_primes = []

from bisect import *

for p in filtered_primes:
	rotation = p
	flag = True
	
	for k in range(len(str(p)) + 2):
		rotation = int(str(rotation)[1:] + str(rotation)[0])
		try:
			if filtered_primes[bisect_left(filtered_primes, rotation)] == rotation:
				continue
			else:
				flag = False
		except:
			flag = False
			
	if flag:
		circle_primes.append(p)
		
print(f'Cirular primes: {len(circle_primes)}')

#print(circle_primes)