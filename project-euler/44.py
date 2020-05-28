from math import sqrt

def pent(n):
	return (3*n*n - n) // 2
	
def good_diff(j, k):
	n = round((1 + sqrt(36*(k**2 - j**2) - 12*(k + j) + 1)) / 6)
	if 3*n*n - n == 3*k*k - k - 3*j*j + j:
		return True
	return False
	
def good_sum(j, k):
	n = round((1 + sqrt(36*(k**2 + j**2) + 12*(k + j) + 1)) / 6)
	if 3*n*n - n == 3*k*k - k + 3*j*j - j:
		return True
	return False
	
cap = 2500
found = False
for j in range(1, cap):
	if found:
		break
		
	for k in range(j + 1, cap):
		diff, plus = False, False
		
		# Break if pj is less than the gap to the next
		if pent(k + 1) - pent(k) > pent(j):
			break
			
		if good_diff(j, k):
			print(j, k, 'diff')
			diff = True
		if good_sum(j, k):
			print(j, k, 'sum')
			plus = True
			
		if diff and plus:
			found=True
			print(pent(k) - pent(j), pent(j), pent(k), pent(j) + pent(k))
			break