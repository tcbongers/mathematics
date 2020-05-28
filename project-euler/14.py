cached_lengths = {}

def chain_length(n):
	length = 1
	while n > 1:
		if n in cached_lengths:
			return cached_lengths[n]
			
		if n % 2 == 0:
			n = n // 2
			length += 1
		else:
			n = 3*n + 1
			length += 1
		
	cached_lengths[n] = length
	return length
		
max_length = 0
for k in range(1, 10**5):
	current_length = chain_length(k)
	if current_length > max_length:
		print(f'{k}, {current_length}')
		max_length = current_length
		