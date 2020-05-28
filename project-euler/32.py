# Can pair a 4 digit number with 1 digit
# Can pair a 3 digit number with 2 digits

products = []

for a in range(1000, 10000):
	for b in range(1, 10):
		if len(str(a) + str(b) + str(a*b)) == 9 and set(str(a) + str(b) + str(a*b)) == set('123456789'):
			print(f'{a} x {b} = {a*b}')
			products.append(a*b)
			
for a in range(100, 1000):
	for b in range(10, 100):
		if len(str(a) + str(b) + str(a*b)) == 9 and set(str(a) + str(b) + str(a*b)) == set('123456789'):
			print(f'{a} x {b} = {a*b}')
			products.append(a*b)
			
print(sum(set(products)))