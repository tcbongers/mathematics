d = '0'
k = 0

while len(d) < 10**6 + 10:
	k += 1
	d += str(k)

prod = 1
for k in range(7):
	prod *= int(d[10**k])
	
print(prod)