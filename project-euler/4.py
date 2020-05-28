max_palindrome = 0

for a in range(900, 1000):
	for b in range(900, 1000): 
		
		max_palindrome = max(max_palindrome, a*b*(str(a*b) == str(a*b)[::-1]))
	
print('Maximum palindrome = ' + str(max_palindrome))