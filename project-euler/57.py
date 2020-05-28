def one():
	return [1, 1]
	
def gcd(a, b):
	while b != 0:
		a, b = b, a % b
	return a
	
def reduce(f):
	g = gcd(f[0], f[1])
	return [f[0] // g, f[1] // g]
	
def add(f1, f2):
	f = [f1[0]*f2[1] + f2[0]*f1[1], f1[1]*f2[1]]
	#print(f)
	return reduce(f)
	
def subtract(f1, f2):
	f = [f1[0]*f2[1] - f2[0]*f2[1], f1[1]*f2[1]]
	return reduce(f)
	
def mult(f1, f2):
	f = [f1[0]*f2[0], f1[1]*f2[1]]
	return reduce(f)
	
def divide(f1, f2):
	f = [f1[0]*f2[1], f1[1]*f2[0]]
	return reduce(f)
	
def invert(f):
	return divide(one(), f)
	
two = [2, 1]

current = two
#print(add(one(), invert(current)))
count = 0

for k in range(1000):
	out = add(one(), invert(current))
	#print(out)
	if len(str(out[0])) > len(str(out[1])):
		count += 1
	current = add(two, invert(current))
	#print(current)
	
print(count)