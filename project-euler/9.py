def get_triplet():

	for a in range(1, 1000):
		for b in range(a + 1, 1000):
			c = 1000 - a - b;
			if c < 0:
				continue
		
			if a*a + b*b == c*c:
				return a*b*c

print(get_triplet())