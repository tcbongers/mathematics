count = 0

for base in range(1, 10):
	for pow in range(100):
		if len(str(base**pow)) == pow:
			print(base**pow)
			count += 1
			
print(count)