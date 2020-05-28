from math import log
primes = [2, 3, 5, 7, 11, 13, 17, 19]
cap = 20
product = 1

for p in primes:
	if p > cap:
		break
		
	product *= p**int(log(cap) / log(p))
	
print('Maximum product = ' + str(product))