from decimal import *
getcontext().prec = 105
s = 0

squares = [n*n for n in range(10)]
for k in range(2, 100):
	if k in squares:
		continue
		
	string= str(Decimal(k).sqrt())
	s += sum(list(map(int, string[0]+string[2:101])))
	
print(s)