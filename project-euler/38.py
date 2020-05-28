# If we have a four digit base, then we just consider n and 2n
# If we have a three digit base, consider n, 2n, 3n
# If we have a two digit base, take n, 2n, 3n, 4n (maybe)
# One digit base -- cannot do better than 918273645

def check(base):
	if len(str(n)) == 4 and len(str(2*n)) == 5:
		if '0' in str(n) + str(2*n):
			return -1
			
		if len((set(str(n)) | set(str(2*n))) - {0}) == 9:
			#print(base, 2*base)
			return int(str(base)+str(2*base))
		
	if len(str(n)) == 3 and len(str(3*n)) == 3:
		if '0' in str(n) + str(2*n) + str(3*n):
			return -1
			
		if len((set(str(n)) | set(str(2*n)) | set(str(3*n))) - {0}) == 9:
			#print(base, 2*base, 3*base)
			return int(str(base) + str(2*base) + str(3*base))
		
	if len(str(n)) == 2 and len(str(3*n)) == 2 and len(str(4*n)) == 3:
		if '0' in str(n) + str(2*n) + str(3*n) + str(4*n):
			return -1
			
		if len((set(str(n)) | set(str(2*n)) | set(str(3*n)) | set(str(4*n))) - {0}) == 9:
			#print(base, 2*base, 3*base, 4*base)
			return int(str(base) + str(2*base) + str(3*base) + str(4*base))
		
	return -1
		
m = 0
for n in range(10**5):
	if check(n) > 0 and check(n) > m:
		print(n)
		m = max(m, check(n))
print(m)