from itertools import permutations

with open('p079_keylog.txt', 'r') as f:
	attempts = [_[:-1] for _ in f.readlines()]	# Strip newline
	
def valid(code, attempt):
	# Check if the attempt is contained in the given code
	# with characters in the correct order
	indices = []
	
	for ch in attempt:
		if ch not in code:
			return False
		indices.append(code.index(ch))
		
	return indices == sorted(indices)
	
# No key contains 4 or 5
codes = list(permutations('01236789', 8))

for a in attempts:
	codes = list(filter(lambda x : valid(x, a), codes))
	if len(codes) == 1:
		print(''.join([_ for _ in codes[0]]))
		break