cap = 4000000

a = 1
b = 1
sum_of_evens = 0

while a < cap:
	a, b = b, a + b
	if a % 2 == 0:
		sum_of_evens += a
	
print('Sum = ' + str(sum_of_evens))