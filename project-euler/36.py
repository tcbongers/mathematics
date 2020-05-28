def is_double_palindrome(number):
	if str(number) == str(number)[::-1]:
		b = bin(number)[2:]
		
		return b == b[::-1]
	
	return False
	
sum_pals = 0

for n in range(10**6):
	if is_double_palindrome(n):
		print(n)
		sum_pals += n
		
print(sum_pals)