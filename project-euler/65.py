from fractions import Fraction as frac

# Generate the representation
repr = [1]
for j in range(1, 40):
	repr += [2*j, 1, 1]
	
#print(repr[0:20])

one = frac(1, 1)
current = frac(repr[-1], 1)
conv = 100
for r in repr[conv - 3::-1]:
	current = one/current + frac(r, 1)
	
current = one/current + one + one

print(f'Convergent {conv}: {current}')
ds = sum([int(a) for a in str(current.numerator)])

print(f'Digit sum = {ds}')