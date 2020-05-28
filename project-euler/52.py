def good(n):
	a = set(str(n))
	if a == set(str(2*n)) and a == set(str(3*n)) and a == set(str(4*n)) and a == set(str(5*n)) and a == set(str(6*n)):
		return True
	return False

n = 1
while True:
	if good(n):
		print(n)
		break
	n += 1