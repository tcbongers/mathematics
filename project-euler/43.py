from itertools import permutations

def good(string):
	int_string = list(map(int, string))
	if int_string[3] % 2 != 0:
		return False
	if (int_string[2] + int_string[3] + int_string[4]) % 3 != 0:
		return False
	if int_string[5] % 5 != 0:
		return False
	if (100*int_string[4] + 10*int_string[5] + int_string[6]) % 7 != 0:
		return False
	if (100*int_string[5] + 10*int_string[6] + int_string[7]) % 11 != 0:
		return False
	if (100*int_string[6] + 10*int_string[7] + int_string[8]) % 13 != 0:
		return False

	return True
	
# Take multiples of 17
k = 1
count = 0
s = 0

while 17*k < 1000:
	end = str(17*k)
	if len(end) < 3:
		end = '0' + end
		
	if len(set(end)) < 3:
		k += 1
		continue
		
	leftover = ''.join([_ for _ in set('0123456789') - set(end)])
	
	# Generate all permutations
	for perm in permutations(leftover, 7):
		string = ''.join(perm) + end
		if good(string):
			print(string)
			count += 1
			s += int(string)
			
	k += 1
print(f'Sum of {count} numbers is {s}')