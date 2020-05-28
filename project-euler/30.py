def power_sum(number, power):
	return sum([int(a)**power for a in str(number)])
		
sum_good = -1

for n in range(9**6):
	if n == power_sum(n, 5):
		print(n)
		sum_good += n
		
print(f'Sum = {sum_good}')
	