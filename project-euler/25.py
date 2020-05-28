a = 1
b = 1
count = 2

while len(str(b)) < 1000:
	b, a = a + b, b
	count += 1

print(count)