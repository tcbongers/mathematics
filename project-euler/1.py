cap = 1000

s = 0

for k in range(1, cap):
	if k % 3 == 0 or k % 5 == 0 and not (k % 15 == 0):
		s += k
	
print('Sum = ' + str(s))